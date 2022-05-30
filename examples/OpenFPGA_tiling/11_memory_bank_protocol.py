"""
============================================
Implementing memeory bank protocol on Tile02
============================================

This example demonstate how to create a tile strcuture from
Verilog netlist obtained from OpenFPGA

.. image:: ../../../examples/OpenFPGA_tiling/_tile02_mb_floorplan.svg
    :height: 400px

"""

import glob
import logging
from pathlib import Path
import tempfile
from itertools import chain
from os import path

import spydrnet as sdn
from spydrnet_physical import PROP
from spydrnet_physical.util import (FloorPlanViz, Tile02,
                                    sram_configuration,
                                    GridFloorplanGen, OpenFPGA)


logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


STYLE_SHEET = '''
    symbol[id*='tile'] * {number:01; fill:#d9d9f3;}
    .over_util {fill:#b22222 !important}
    text{font-family: Lato; font-size: 15px;}
'''


def main():
    proj = '../homogeneous_k6n10_standalone_fabric'
    source_files = glob.glob(f'{proj}/*_Verilog/lb/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/routing/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/sub_module/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/fpga_top.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for each_verilog in source_files:
            with open(each_verilog, "r", encoding="UTF-8") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    fpga = OpenFPGA(grid=[4, 4], netlist=netlist)
    fpga.design_top_stat()

    # Convert wires to bus structure
    fpga.create_grid_clb_bus()
    fpga.create_grid_io_bus()
    fpga.create_sb_bus()
    fpga.create_cb_bus()

    # Remove undriven nets
    fpga.remove_undriven_nets()
    fpga.remove_config_chain()

    # Convert top level independent nets to bus
    for i in chain(fpga.top_module.get_instances("grid_clb*"),
                   fpga.top_module.get_instances("grid_io*"),
                   fpga.top_module.get_instances("sb_*")):
        for p in filter(lambda x: True, i.reference.ports):
            if p.size > 1 and (i.check_all_scalar_connections(p)):
                cable_list = []
                for pin in p.pins[::-1]:
                    cable_list.append(i.pins[pin].wire.cable)
                cable = fpga.top_module.combine_cables(
                    f"{i.name}_{p.name}", cable_list)
                cable.is_downto = False

    # Before Creating Tiles
    # fpga.design_top_stat()

    # Merge grid IOs
    fpga.merge_all_grid_ios()
    # Create area-optimized tiles
    fpga.register_tile_generator(Tile02)
    fpga.create_tiles()
    merge_wl_bl_ports(fpga)

    # Add configuration circuit
    logger.handlers[0].setLevel(logging.DEBUG)
    fpga.register_config_generator(sram_configuration)
    # fpga.config_creator.print_configuration_bit_matrix()
    fpga.config_creator.set_wl_distribution([4, 4, 4, 4, 4])
    print(f"word_line_rows = {fpga.config_creator.word_line_rows}")
    print(f"bit_line_cols  = {fpga.config_creator.bit_line_cols}")
    fpga.add_configuration_scheme()
    logger.handlers[0].setLevel(logging.INFO)

    # After Creating Tiles
    # fpga.design_top_stat()

    for each in fpga.top_module.get_definitions("*"):
        each.properties["LABEL"] = each.properties.get("CONFIG_BITS", 0)

# %%
#
# Following section is for rendering only
#

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #           Floorplan visualization
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    # Create grid plan
    grid_plan = GridFloorplanGen(5, 5, grid_x=220, grid_y=220)

    grid_plan.offset_x = 10
    grid_plan.offset_y = 10
    grid_plan.set_column_width(1, 120)
    grid_plan.set_row_height(1, 120)

    for module in fpga.top_module.get_definitions("*tile*"):
        module.data[PROP]["WIDTH"] = 200
        module.data[PROP]["HEIGHT"] = 200
        module.data[PROP]["COLOR"] = "#E6BA95"

    for module in fpga.top_module.get_definitions("*bottom*tile"):
        module.data[PROP]["HEIGHT"] = 100

    for module in fpga.top_module.get_definitions("*left*tile"):
        module.data[PROP]["WIDTH"] = 100

    for xi in range(5, 0, -1):
        for yi in range(5, 0, -1):
            x_offset, y_offset = 10, 10
            points = grid_plan.get_x_y(xi-1, yi-1)
            try:
                inst = next(fpga.top_module.get_instances(f"*_{xi}__{yi}_*"))
            except StopIteration:
                continue

            inst.data[PROP]['LOC_X'] = points[0] + x_offset
            inst.data[PROP]['LOC_Y'] = points[1] + y_offset

    fpga.top_module.data[PROP]["WIDTH"] = grid_plan.width + 20
    fpga.top_module.data[PROP]["HEIGHT"] = grid_plan.height + 20

    fpga.save_shaping_data("*", scale=0.01, filename="_tile01_shaping.txt")

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #                   Visualize floorplan
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    fp = FloorPlanViz(fpga.top_module)
    fp.compose(skip_connections=True, skip_pins=True)
    fp.custom_style_sheet = STYLE_SHEET
    dwg = fp.get_svg()
    dwg.add(grid_plan.render_grid(return_group=True))
    dwg.saveas("_tile02_mb_floorplan.svg", pretty=True, indent=4)

    # Save netlist
    base_dir = "output_tile01"
    Path(base_dir).mkdir(parents=True, exist_ok=True)
    fpga.save_netlist("sb*", path.join(base_dir, "routing"))
    fpga.save_netlist("cb*", path.join(base_dir, "routing"))
    fpga.save_netlist("grid*", path.join(base_dir, "lb"))
    fpga.save_netlist("*tile*", path.join(base_dir, "tiles"))
    fpga.save_netlist("fpga_top", path.join(base_dir))


def merge_wl_bl_ports(fpga: OpenFPGA):
    W, H = fpga.fpga_size
    for module in fpga.top_module.get_definitions("*"):
        bl_ports = list(module.get_ports("bl*"))
        if bl_ports:
            for bl in bl_ports[::-1]:
                module.split_port(bl)
            module.combine_ports("bl", list(module.get_ports("bl*"))[::-1])
        wl_ports = list(module.get_ports("wl*"))
        if wl_ports:
            for wl in wl_ports[::-1]:
                module.split_port(wl)
            module.combine_ports("wl", list(module.get_ports("wl*"))[::-1])


if __name__ == "__main__":
    main()

# %%
#
# Output Shaping File
# ^^^^^^^^^^^^^^^^^^^^
#
# .. literalinclude:: ../../../examples/OpenFPGA_tiling/_tile01_shaping.txt
#
#
