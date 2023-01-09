"""
This script translates the GSB data exported from OpnFPGA engine to the desired
format
"""

import argparse
import fileinput
import glob
import json
import shutil
import os
import pathlib
import xml.etree.ElementTree as ET
from copy import deepcopy

import spydrnet as sdn
import yaml


def formatter(prog):
    return argparse.HelpFormatter(prog, max_help_position=60)


def parse_argument() -> argparse.Namespace:
    parser = argparse.ArgumentParser(formatter_class=formatter)
    parser.add_argument(
        "--instance_map", help="jsonfile_containing instace map")
    parser.add_argument("--top_level_design", help="Design name")
    parser.add_argument("--gsb_dir", type=str, help="General switch box dir")
    return parser.parse_args()


def extract_input(root):
    # Create new Input Tag
    input_conn = ET.Element("INPUT")
    # Add input connection details
    for chan in ["CHANX", "CHANY", "OPIN"]:
        channel = ET.Element(chan)
        for each in sorted(
            set(
                [
                    f"{ele.attrib['side']}_{int(ele.attrib['index']):03}"
                    for ele in root.findall(f".//driver_node[@type='{chan}']")
                ]
            )
        ):
            each = each.split("_")
            elements = root.findall(
                f".//driver_node[@type='{chan}'][@side='{each[0]}'][@index='{int(each[1])}']"
            )
            element = deepcopy(elements[0])
            element.attrib["connections"] = str(len(elements))
            elements = root.findall(
                f".//driver_node[@type='{chan}'][@side='{each[0]}'][@index='{int(each[1])}']/.."
            )
            element.attrib["out_driver"] = str(
                len([e for e in elements if e.attrib["mux_size"] == "0"])
            )
            channel.append(element)
        input_conn.append(channel)
    return input_conn


def clean_tags(root):
    # Drop segment_id and node_id attributes
    for ele in root.findall("*") + root.findall(".//driver_node"):
        if "segment_id" in ele.attrib.keys():
            ele.attrib.pop("segment_id")
        if "sb_module_pin_name" in ele.attrib.keys():
            ele.attrib.pop("sb_module_pin_name")
        if "node_id" in ele.attrib.keys():
            ele.attrib.pop("node_id")


def clean_gsb(instance_map, top_level_design, gsb_dir):
    """
    Main method to clean general switch box
    """
    if instance_map:
        instance_list = json.load(open(instance_map, "r", encoding="UTF-8"))
    elif top_level_design:
        # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
        # Read FPGA Netlist
        # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
        netlist = sdn.parse(top_level_design)

        # Create instance and reference mapping
        instance_list = {}
        for each in netlist.get_instances("*__*"):
            if not each.reference.name in instance_list.keys():
                instance_list[each.reference.name] = []
            instance_list[each.reference.name].append(each.name)
    else:
        return

    for _, file in enumerate(sorted(glob.glob(f"{gsb_dir}/_*.xml"))):
        module = os.path.splitext(os.path.basename(file))[0]
        # =====================================================================
        # Extract Switch Box information
        # =====================================================================
        tree = ET.parse(file)
        root = tree.getroot()
        clean_tags(root)
        # Remove IPINs
        for ele in root.findall("IPIN"):
            root.remove(ele)
        root.append(extract_input(root))
        root.attrib["type"] = "SB"
        tree.write(f"{gsb_dir}/{module[1:]}.xml", encoding="utf-8")
        print(f"Writing {file}")
        continue
        # =====================================================================
        # Extract Connection Box horizontal information
        # =====================================================================
        tree = ET.parse(file)
        root = tree.getroot()
        clean_tags(root)
        for tag in ["CHANX", "CHANY", "IPIN[@side='left']", "IPIN[@side='right']"]:
            for ele in root.findall(tag):
                root.remove(ele)
        if len(list(root)) > 1:
            filename = module.replace("sb", "cbx")[1:]
            filename = [ref for ref, inst in instance_list.items() if filename in inst][
                0
            ]
            root.append(extract_input(root))
            root.attrib["type"] = "CBX"
            tree.write(f"{gsb_dir}/{filename}.xml")

        # =====================================================================
        # Extract Connection Box Vertical information
        # =====================================================================
        tree = ET.parse(file)
        root = tree.getroot()
        clean_tags(root)
        for tag in ["CHANX", "CHANY", "IPIN[@side='top']", "IPIN[@side='bottom']"]:
            for ele in root.findall(tag):
                root.remove(ele)
        module = module.split("_")
        module[4] = str(int(module[4]) + 1)
        module = "_".join(module)
        filename = module.replace("sb", "cby")[1:]
        if len(list(root)) > 1:
            filename = [ref for ref, inst in instance_list.items() if filename in inst][
                0
            ]
            root.append(extract_input(root))
            root.attrib["type"] = "CBY"
            tree.write(f"{gsb_dir}/{filename}.xml")


def split_fabric_bitstream(fabric_file, instance_list, output_dir="_split_bitstreams"):
    tree = ET.parse(fabric_file)
    root = tree.getroot()

    instance_map = yaml.safe_load(open(instance_list, "r", encoding="UTF-8"))

    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
    with open(f"{output_dir}/instance_sequence.yaml", "w", encoding="UTF-8") as fp:
        yaml.safe_dump(list(map(lambda x: x.attrib["name"], list(root))), fp)
    print(f"{output_dir}/instance_sequence.yaml saved")

    visited = []
    for ele in list(root):
        instance_name = ele.attrib["name"]
        module_name = [m for m, inst in instance_map.items()
                       if instance_name in inst][0]

        # out_directory = f'{output_dir}' if unique else f'{output_dir}/{module_name}'
        out_directory = f'{output_dir}/{module_name}'
        out_filename = f'{module_name}'
        out_xml_file = f"{out_directory}/{out_filename}_bits.xml"
        pathlib.Path(out_directory).mkdir(parents=True, exist_ok=True)

        if not module_name in visited:
            # Save bitsream section
            ET.ElementTree(ele).write(out_xml_file, encoding="unicode")

            for line in fileinput.input(out_xml_file, inplace=True):
                print(line.replace(instance_name, "{{INSTACE_NAME}}"), end="")

            # Create list of paths in correct sequence
            print_format = ""
            with open(f"{out_directory}/{out_filename}_paths.txt", "w", encoding="UTF-8") as fp:
                for indx, h_ele in enumerate(ele.findall(".//hierarchy/..")):
                    path = ".".join([e.attrib["name"]
                                    for e in h_ele.findall(".//instance")])
                    bit_len = len(h_ele.findall(".//bit"))
                    fp.write(f"{indx+1:3}. [{bit_len:3}] " +
                             path.rsplit(instance_name, 1)[-1]+"\n")
                    # print_format += f"%{max(bit_len,7)}s" %
                    print_format += f" {f'[{indx+1}]':>{max(bit_len,7)}}"

        # Store bitstream values
        with open(f"{out_directory}/{out_filename}_bitstream.txt", "a", encoding="UTF-8") as fp:
            if not module_name in visited:
                fp.write(f"{'':15} |" + print_format + "\n")
            bits = []
            for indx, h_ele in enumerate(ele.findall(".//hierarchy/..")):
                bits_words = "".join([mems.attrib["value"]
                                     for mems in h_ele.findall(".//bit")])
                bits.append(f" {bits_words:>{max(len(bits_words),7)}}")
            fp.write(f"{instance_name:15} |" + "".join(bits) + "\n")
        visited.append(module_name)


def _prepare_bitstream_block(instance_name, bitstream_template, bitstream):
    shutil.copy2(bitstream_template, "_tmp_bitstream_template.xml")
    for line in fileinput.input("_tmp_bitstream_template.xml", inplace=True):
        print(line.replace("{{INSTACE_NAME}}", instance_name), end="")

    tree = ET.parse(open("_tmp_bitstream_template.xml", "r", encoding="UTF-8"))
    root = tree.getroot()
    return root


def merge_fabric_bitstream(fabric_file, instance_list, output_dir="_split_bitstreams"):

    instance_map = yaml.safe_load(open(instance_list, "r", encoding="UTF-8"))

    bitstreams = {}

    for module_name in instance_map.keys():
        print(f" -------- {module_name} -------- ")
        try:
            bitfile_name = f"{output_dir}/{module_name}/{module_name}_bitstream.txt"
            with open(bitfile_name, "r", encoding="UTF-8") as fp:
                for lines in fp.readlines()[1:]:
                    instance, bits = lines.rsplit("|")
                    instance = instance.strip()
                    bitstreams[instance] = _prepare_bitstream_block(
                        instance, f"{output_dir}/{module_name}/{module_name}_bits.xml",
                        bits.replace(" ", ""))
            print(f"Done {instance}")
        except FileNotFoundError:
            print(f"{module_name} bitstream block not found")

    # Create top level bitstream again
    tree = ET.Element("bitstream_block", attrib={
                      "name": "fpga_top", "hierarchy_level": "0"})
    filename = f"{output_dir}/instance_sequence.yaml"
    with open(filename, "r", encoding="UTF-8") as fp:
        for instance in yaml.safe_load(fp):
            # tree.append( ET.Element("bitstream_block",
            #             attrib={"name": instance}))
            tree.append(bitstreams[instance])

    ET.ElementTree(tree).write(fabric_file)
    # with open(fabric_file, "w", encoding="UTF-8") as fp:
    #     fp.write("This file is auto generated")


def generate_sdc_constraints(fabric_file, instance_list, output_dir="_constraints"):
    pass


if __name__ == "__main__":
    args = parse_argument()
    clean_gsb(args.instance_map, args.top_level_design, args.gsb_dir)
    split_fabric_bitstream(
        "../examples/homogeneous_fabric/FPGA44_bitstreams/top/fabric_independent_bitstream.xml",
        "../examples/homogeneous_fabric/top_hierarchy.yml")
