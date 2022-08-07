"""
=============================
OpenFPGA architecture parsing
=============================

This example demonstrates the ``OpenFPGA_Arch`` class which parses the
`VPR` and `OpenFPGA` Architecture file and provides logical information.

"""
import os
import logging
import spydrnet as sdn
from spydrnet_physical.util import OpenFPGA_Arch

# Enable output logging
logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO", filename="01_fpga_arch_parse")

# Read OpenFPGA and VPR architectue file
task_dir = ("..", "homogeneous_fabric", "FPGA44_Task")
vpr_arch = os.path.join(*task_dir, "arch", "k6_N10_tileable.xml")
openfpga_arch = os.path.join(*task_dir, "arch", "k6_N10_openfpga.xml")
fpga_arch = OpenFPGA_Arch(vpr_arch, openfpga_arch, layout="4x4")

# Print avaialble layouts and pb_types in the file
logger.info(fpga_arch.get_layouts())
logger.info(fpga_arch.pb_types)
# logger.info(fpga_arch.is_homogeneous())

# %%
# Output
# ------
#
# .. literalinclude:: ../../../examples/OpenFPGA_basic/_01_fpga_arch_parse_spydrnet.log
#
#
