"""
==================================
Heterogeneous Floorplan Adjustment
==================================

This example customises the hterogeneous placement and demonstrate how perticular
column or row of the FPGa grid can be cpmpressed.

**Pre Tile Render**

.. image:: ../../../examples/OpenFPGA_Floorplanning/_hetero_pre_tile.svg
   :width: 70%
   :align: center

**Post Tile Render**

.. image:: ../../../examples/OpenFPGA_Floorplanning/_hetero_tile.svg
   :width: 70%
   :align: center

"""

import glob
import logging
import math
import json
from collections import OrderedDict
from copy import deepcopy

import spydrnet as sdn
from spydrnet_physical.util import (
    FloorPlanViz,
    FPGAGridGen,
    OpenFPGA,
    Tile02,
    get_names,
    initial_hetero_placement,
)

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO", filename="floorplan_heterpgeneous")


CBX_COLOR = "#d9d9f3"
CBY_COLOR = "#a8d0db"
SB_COLOR = "#ceefe4"
GRID_COLOR = "#ddd0b1"
HETERO_COLOR = "#6E6858"

FPGA_WIDTH = 8
FPGA_HEIGHT = 8

SCALE = 100
CPP = math.floor(0.46 * SCALE)
SC_HEIGHT = math.floor(2.72 * SCALE)

STYLE_SHEET = """
    symbol {mix-blend-mode: difference;}
    symbol[id*='mult'] * {number:01; fill:#BC85C3;}
    symbol[id*='mult_mid'] * {number:01; fill:#0085C3;}
    symbol[id*='mult_right'] * {number:01; fill:#FFD39A;}
    symbol[id*='mult_mid'] * {number:01; fill:#0A45C3;}
    symbol[id*='mult_right_mid'] * {number:01; fill:#DF7861;}
    symbol[id*='mult_top'] * {number:01; fill:#80558C;}
    symbol[id*='mult_right_top'] * {number:01; fill:#A27B5C;}
    .over_util {fill:#b22222 !important}
    text{font-family: Lato; font-style: italic; font-size: 750px;}
    rect.highlight_box { fill:none; stroke-width:40; stroke:green;}
    text.highlight_box { font-size:500px; font-weight:800; fill:red}
"""

MULT_COLS = [2, 8]


def main():
    """
    Main method
    """

    proj = "../heterogeneous_fabric/"
    source_files = glob.glob(f"{proj}/*_Verilog/lb/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/routing/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/sub_module/*.v")
    source_files += glob.glob(f"{proj}/*_Verilog/fpga_top.v")

    # Create OpenFPGA object
    fpga = OpenFPGA(grid=(8, 8), verilog_files=source_files)

    # Convert wires to bus structure
    fpga.merge_all_grid_ios()
    fpga.design_top_stat()

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #           Floorplan visualization
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

    fpga_grid = FPGAGridGen(
        design_name="FPGA8x8",
        layout="8x8",
        arch_file=f"{proj}/FPGA88_hetero_Task/arch/k6_N10_tileable.xml",
        release_root=None,
    )
    fpga_grid.enumerate_grid()
    fpga.load_grid(fpga_grid)
    fpga.annotate_area_information(f"{proj}/area_info.txt", skipline=1)

    fpga.SC_HEIGHT = SC_HEIGHT
    fpga.CPP = CPP
    fpga.SC_GRID = CPP * SC_HEIGHT

    # = = = = = = = = = = = = = = = = = = = = = = =
    #         Shaping Information
    # = = = = = = = = = = = = = = = = = = = = = = =

    fpga.register_placement_creator(initial_hetero_placement)

    m = {}
    m["clb_w"], m["clb_h"] = 340, 48
    m["cbx11_w"], m["cbx11_h"] = 340, 18
    m["bottom_cbx_w"], m["bottom_cbx_h"] = 340, 18
    m["top_cbx_w"], m["top_cbx_h"] = 340, 40

    m["cby11_w"], m["cby11_h"] = 120, 48
    m["left_cby_w"], m["left_cby_h"] = 180, 48
    m["right_cby_w"], m["right_cby_h"] = 160, 48

    m["mult_w_delta"] = 120

    fpga.placement_creator.update_shaping_param(m)
    fpga.placement_creator.derive_sb_paramters()
    fpga.placement_creator.create_shapes()

    shapes = fpga.placement_creator.module_shapes

    # This adjusts the placement grid
    for col in MULT_COLS:
        fpga.placement_creator.design_grid.set_column_width(
            col * 2, (m["clb_w"] - m["mult_w_delta"]) * CPP
        )

    inst = fpga.design_top_stat()
    logger.info("This are extra modules to floorplan")
    logger.info(set(inst.keys()) - set(shapes.keys()))

    shapes["cbx_2__0_"] = deepcopy(shapes["cbx_1__0_"])
    shapes["cbx_2__0_"]["POINTS"][0] -= m["mult_w_delta"]
    shapes["cbx_2__2_"] = deepcopy(shapes["cbx_1__1_"])
    shapes["cbx_2__2_"]["POINTS"][0] -= m["mult_w_delta"]
    shapes["cbx_2__8_"] = deepcopy(shapes["cbx_1__8_"])
    shapes["cbx_2__8_"]["POINTS"][0] -= m["mult_w_delta"]
    shapes["cby_2__1_"] = deepcopy(shapes["cby_1__1_"])
    shapes["cby_3__1_"] = deepcopy(shapes["cby_1__1_"])
    shapes["sb_1__2_"] = deepcopy(shapes["sb_1__1_"])
    shapes["sb_2__0_"] = deepcopy(shapes["sb_1__0_"])
    shapes["sb_2__1_"] = deepcopy(shapes["sb_1__1_"])
    shapes["sb_2__2_"] = deepcopy(shapes["sb_1__1_"])
    shapes["sb_2__8_"] = deepcopy(shapes["sb_1__8_"])
    shapes["sb_3__0_"] = deepcopy(shapes["sb_1__0_"])
    shapes["sb_3__1_"] = deepcopy(shapes["sb_1__1_"])
    shapes["sb_3__8_"] = deepcopy(shapes["sb_1__8_"])
    shapes["sb_8__2_"] = deepcopy(shapes["sb_8__1_"])

    shapes["grid_mult_8"] = deepcopy(shapes["grid_clb"])
    shapes["grid_mult_8"]["POINTS"][1] += m["clb_h"] + m["cbx11_h"]
    shapes["grid_mult_8"]["POINTS"][0] -= m["mult_w_delta"]

    shapes["sb_2__1_"]["POINTS"][1] = 0  # Trim right side
    shapes["sb_2__1_"]["PLACEMENT"][0] = 0  # Reset x offset
    shapes["sb_8__1_"]["POINTS"][1] = 0  # Trim right side
    shapes["sb_8__1_"]["PLACEMENT"][0] = 0  # Reset x offset

    # Make few modules unique to fit in floorplan
    inst_list = []
    for col in MULT_COLS:
        inst_list += [f"sb_{col-1}__{i}_" for i in range(1, FPGA_HEIGHT, 2)]
    fpga.top_module.make_instance_unique(
        next(fpga.top_module.get_instances(inst_list[0])),
        "sb_7__1_",
        instance_list=inst_list,
    )
    shapes["sb_7__1_"] = deepcopy(shapes["sb_1__1_"])
    shapes["sb_7__1_"]["POINTS"][-2] = 0  # Trim right side
    shapes.pop("sb_1__1_")

    fpga.create_placement()
    fpga.update_module_label()

    additional_styles = fpga.get_overutils_styles()

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    fpga.show_placement_data("*")

    fp = FloorPlanViz(fpga.top_module)
    fp.compose(skip_connections=True, skip_pins=True)
    fp.custom_style_sheet = STYLE_SHEET + additional_styles
    dwg = fp.get_svg()
    dwg.add(fpga.placement_creator.design_grid.render_grid(return_group=True))

    pattern = dwg.pattern(size=(4 * CPP, 2 * SC_HEIGHT), patternUnits="userSpaceOnUse")
    pattern.add(dwg.circle(center=(2, 2), r=1, fill="black"))
    pattern.add(dwg.circle(center=(2, SC_HEIGHT + 2), r=1, fill="red"))
    dwg.defs.add(pattern)
    dwg.defs.elements[0].elements[0].attribs["fill"] = pattern.get_funciri()

    filename = "_hetero_pre_tile.svg"
    dwg.saveas(filename, pretty=True, indent=4)

    # = = = = = = = = = = = = Create Tile = = = = = = = = = = = =
    fpga.register_tile_generator(Tile02)
    fpga.create_tiles()
    merge_inter_hetero_routing(
        fpga,
        "sb_8__2_",
        prefix="_fp",
        new_def_name="grid_mult_right_mid",
        merge_instance=["cbx_{x}__{y}_"],
    )
    merge_inter_hetero_routing(
        fpga,
        "sb_2__2_",
        prefix="_fp",
        new_def_name="grid_mult_mid",
        merge_instance=["cbx_{x}__{y}_"],
    )
    merge_inter_hetero_routing(
        fpga,
        "sb_8__8_",
        prefix="_fp",
        new_def_name="grid_mult_right_top",
        merge_instance=["cbx_{x}__{y}_"],
    )
    merge_inter_hetero_routing(
        fpga,
        "sb_2__8_",
        prefix="_fp",
        new_def_name="grid_mult_top",
        merge_instance=["cbx_{x}__{y}_"],
    )
    merge_inter_hetero_routing(
        fpga,
        "sb_8__1_",
        prefix="_fp",
        new_def_name="grid_mult_right",
        merge_instance=["cby_{x}__{y}_", "cby_{x}__{y1}_", "grid_mult_8_{x}__{y}_"],
    )
    merge_inter_hetero_routing(
        fpga,
        "sb_2__1_",
        prefix="_fp",
        new_def_name="grid_mult",
        merge_instance=["cby_{x}__{y}_", "cby_{x}__{y1}_", "grid_mult_8_{x}__{y}_"],
    )

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # fpga.show_placement_data("*")

    fp = FloorPlanViz(fpga.top_module)
    fp.compose(skip_connections=True, skip_pins=True)
    fp.custom_style_sheet = STYLE_SHEET + additional_styles
    dwg = fp.get_svg()
    dwg.add(fpga.placement_creator.design_grid.render_grid(return_group=True))

    pattern = dwg.pattern(size=(4 * CPP, 2 * SC_HEIGHT), patternUnits="userSpaceOnUse")
    pattern.add(dwg.circle(center=(2, 2), r=1, fill="black"))
    pattern.add(dwg.circle(center=(2, SC_HEIGHT + 2), r=1, fill="red"))
    dwg.defs.add(pattern)
    dwg.defs.elements[0].elements[0].attribs["fill"] = pattern.get_funciri()

    filename = "_hetero_tile.svg"
    dwg.saveas(filename, pretty=True, indent=4)

    filename = "_top_instances_ports.txt"
    dump_top_definition_ports(fpga, rpt_file=filename)


def sort_by_cordinate(inst_name):
    """
    Get the cordinates from the intance name
    """
    x = int(inst_name.split("_")[-4])
    y = int(inst_name.split("_")[-2])
    return f"{x:05}{y:05}"


def merge_inter_hetero_routing(
    fpga, block_name, prefix="_old", new_def_name=None, merge_instance=None
):
    """
    This method merges arouting beetween heterogeneous module
    """
    instance_list = []
    instance = next(fpga.top_module.get_definitions(f"*{block_name}*")).references
    instance = get_names(list(instance))
    for block_name in sorted(instance, key=sort_by_cordinate):
        block = next(fpga.top_module.get_instances(block_name))
        x = int(block.name.split("_")[-4])
        y = int(block.name.split("_")[-2])
        group = [block]
        for inst in merge_instance:
            group.append(
                next(
                    fpga.top_module.get_instances(
                        inst.format(x=x, y=y, x_1=x - 1, y_1=y - 1, x1=x + 1, y1=y + 1)
                    )
                )
            )
        instance_list.append((group, group[0].name + "_new"))
        logger.debug("Merging %s", " ".join([n.name for n in group]))
    new_module_name = instance_list[0][0][0].reference.name + "_new"
    main_def, instance_list = fpga.top_module.merge_multiple_instance(
        instance_list, new_definition_name=new_module_name
    )
    main_def.OptPins()
    next(fpga.library.get_definitions(main_def.name[:-4])).name += prefix
    main_def.name = new_def_name or main_def.name[:-4]
    for inst in instance_list:
        inst.name = inst.name[:-4]


def dump_top_definition_ports(fpga: OpenFPGA, rpt_file):
    """
    Create top level port
    """
    portmap = OrderedDict()
    instances = {t.name: t for t in fpga.top_module.get_definitions()}
    instances = OrderedDict(sorted(instances.items(), reverse=True))
    for def_name, defs in instances.items():
        if "ASSIGN" in def_name:
            continue
        if def_name.startswith("const"):
            continue
        portmap[def_name] = sorted(get_names(defs.get_ports("*")))

    json.dump(portmap, open(rpt_file, "w", encoding="UTF-8"), indent=4)


if __name__ == "__main__":
    main()
