"""
This script translates the GSB data exported from OpnFPGA engine to the desired
format
"""

import argparse
import glob
import json
import os
import xml.etree.ElementTree as ET
from copy import deepcopy

import spydrnet as sdn


def formatter(prog):
    return argparse.HelpFormatter(prog, max_help_position=60)


def parse_argument() -> argparse.Namespace:
    parser = argparse.ArgumentParser(formatter_class=formatter)
    parser.add_argument("--instance_map", help="jsonfile_containing instace map")
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


if __name__ == "__main__":
    args = parse_argument()
    clean_gsb(args.instance_map, args.top_level_design, args.gsb_dir)
