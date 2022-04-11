"""
This script translates the GSB data exported from OpnFPGA engine to the desired
format
"""

import glob
import os
from copy import deepcopy
import tempfile
import spydrnet as sdn
import xml.etree.ElementTree as ET


def extract_input(root):
    # Create new Input Tag
    input_conn = ET.Element('INPUT')
    # Add input connection details
    for chan in ["CHANX", "CHANY", "OPIN"]:
        channel = ET.Element(chan)
        for each in sorted(set([f"{ele.attrib['side']}_{ele.attrib['index']}" for ele in root.findall(f".//driver_node[@type='{chan}']")])):
            each = each.split("_")
            elements = root.findall(
                f".//driver_node[@type='{chan}'][@side='{each[0]}'][@index='{each[1]}']")
            element = deepcopy(elements[0])
            element.attrib["connections"] = str(len(elements))
            channel.append(element)
        input_conn.append(channel)
    return input_conn


def clean_tags(root):
    # Drop segment_id and node_id attributes
    for ele in root.findall("*") + root.findall(".//driver_node"):
        if 'segment_id' in ele.attrib.keys():
            ele.attrib.pop("segment_id")
        if 'sb_module_pin_name' in ele.attrib.keys():
            ele.attrib.pop("sb_module_pin_name")
        ele.attrib.pop("node_id")


def main():
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # Read FPGA Netlist
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    proj = 'FPGA88_hetero_Verilog'
    gsb = 'FPGA88_hetero_gsb'
    source_files = []
    source_files += glob.glob(f'{proj}/fpga_top.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for eachV in source_files:
            with open(eachV, "r") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    # Create instance and reference mapping
    instance_list = {}
    for each in netlist.get_instances("*__*"):
        if not each.reference.name in instance_list.keys():
            instance_list[each.reference.name] = []
        instance_list[each.reference.name].append(each.name)

    for indx, file in enumerate(sorted(glob.glob(f'{gsb}/_*.xml'))):
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
        tree.write(f"{gsb}/{module[1:]}.xml", encoding="utf-8")

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
            filename = [ref for ref, inst in instance_list.items()
                        if filename in inst][0]
            root.append(extract_input(root))
            root.attrib["type"] = "CBX"
            tree.write(f"{gsb}/{filename}.xml")

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
        module[4] = str(int(module[4])+1)
        module = "_".join(module)
        filename = module.replace("sb", "cby")[1:]
        if len(list(root)) > 1:
            filename = [ref for ref, inst in instance_list.items()
                        if filename in inst][0]
            root.append(extract_input(root))
            root.attrib["type"] = "CBY"
            tree.write(f"{gsb}/{filename}.xml")


if __name__ == "__main__":
    main()
