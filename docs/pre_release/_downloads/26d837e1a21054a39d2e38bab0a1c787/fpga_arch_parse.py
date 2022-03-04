
"""
OpenFPGA architecture Parsing
=============================

"""
import os
from spydrnet_physical.util import OpenFPGA_Arch

vpr_arch = os.path.join('..', 'homogeneous_fabric', 'FPGA44_Task',
                        'arch', 'k6_N10_tileable.xml')
openfpga_arch = os.path.join('..', 'homogeneous_fabric', 'FPGA44_Task',
                             'arch', 'k6_N10_openfpga.xml')
fpga_arch = OpenFPGA_Arch(vpr_arch, openfpga_arch)

print(fpga_arch.get_layout())
print(fpga_arch.pb_types)
