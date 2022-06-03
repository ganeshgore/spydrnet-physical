"""
===================================
Renaming Homogeneous FPGA Modules
===================================

Demonstrates how to rename FPGA modules

"""

import glob
import logging
import tempfile

import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


def main():
    proj = "../homogeneous_fabric"
    source_files = glob.glob(f'{proj}/*_Verilog/lb/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/routing/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/sub_module/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/fpga_top.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for each_module in source_files:
            with open(each_module, "r") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    fpga = OpenFPGA(grid=(4, 4), netlist=netlist)

    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    #           Renaming Module
    # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
    rename_modules_map = {
        "grid_clb": "LB",
        "cbx_1__1_": "h_conn",
        "cby_1__1_": "v_conn"
    }
    for each_module, new_name in rename_modules_map.items():
        next(fpga.top_module.get_definitions(each_module)).name = new_name

    fpga.design_top_stat()


if __name__ == "__main__":
    main()
