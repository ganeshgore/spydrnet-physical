"""
===================================
Renaming Homogeneous FPGA Modules
===================================

Demonstrates how to rename FPGA modules

"""

from glob import glob
import logging

import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


proj = "../homogeneous_fabric"
source_files = glob(f'{proj}/*_Verilog/lb/*.v')
source_files += glob(f'{proj}/*_Verilog/routing/*.v')
source_files += glob(f'{proj}/*_Verilog/sub_module/*.v')
source_files += glob(f'{proj}/*_Verilog/fpga_top.v')

# Create OpenFPGA object
fpga = OpenFPGA(grid=(4, 4), verilog_files=source_files)
fpga.design_top_stat(filename="_before_rename.txt")

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#           Renaming Module
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
rename_modules_map = {
    "grid_clb": "logic_block",
    "cbx_1__1_": "h_conn",
    "cby_1__1_": "v_conn"
}
for each_module, new_name in rename_modules_map.items():
    next(fpga.top_module.get_definitions(each_module)).name = new_name

fpga.design_top_stat(filename="_after_rename.txt")


# %%
# **Output**
#
# **before_rename**
#
# .. literalinclude:: ../../../examples/OpenFPGA_basic/_before_rename.txt
#
# **after_rename**
#
# .. literalinclude:: ../../../examples/OpenFPGA_basic/_after_rename.txt
