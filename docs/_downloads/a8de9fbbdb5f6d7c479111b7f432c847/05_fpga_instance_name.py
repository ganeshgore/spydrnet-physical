"""
================================
FPGA Instance to Layout mapping 
================================

"""

import glob
import logging
import tempfile

import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA, FPGAGridGen

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
        for eachV in source_files:
            with open(eachV, "r") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    fpga = OpenFPGA(grid=(4, 4), netlist=netlist)

    fpga_grid = FPGAGridGen(design_name='FPGA4x4', layout="4x4",
                            arch_file=f"{proj}/FPGA44_Task/arch/k6_N10_tileable.xml",
                            release_root=None)
    fpga_grid.enumerate_grid()
    fpga.load_grid(fpga_grid)

    for y in range(9, 0, -1):
        for x in range(1, 9+1):
            print(f"{fpga.get_top_instance(x, y):10}", end="")
        print("")


if __name__ == "__main__":
    main()
