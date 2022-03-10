
"""
OpenFPGA Architecture Parsing
=============================

This example demonstrates the ``OpenFPGA_Arch`` class which parses the 
`VPR` and `OpenFPGA` Architecture file and provides logical information.

"""
import os
from spydrnet_physical.util import OpenFPGA_Arch

task_dir = ('..', 'homogeneous_fabric', 'FPGA44_Task')
vpr_arch = os.path.join(*task_dir, 'arch', 'k6_N10_tileable.xml')
openfpga_arch = os.path.join(*task_dir, 'arch', 'k6_N10_openfpga.xml')
fpga_arch = OpenFPGA_Arch(vpr_arch, openfpga_arch)

print(fpga_arch.get_layouts())
print(fpga_arch.pb_types)
