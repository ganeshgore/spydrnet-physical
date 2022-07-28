"""
============================================
Fabric key generation for homogeneous fabric
============================================

This example shows how to generate fabric key for given architecture

**Fabric key on homogeneous fabric**

.. image:: ../../../examples/OpenFPGA_config/_small_layout_ccff_fabric_render.svg
   :width: 80%
   :align: center

"""


import logging

import spydrnet as sdn
from spydrnet_physical.util import FPGAGridGen, FabricKeyGenCCFF

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")

fpga = FPGAGridGen(
    design_name="example_design",
    arch_file="../OpenFPGA_basic/support_files/vpr_arch_render_demo.xml",
    release_root="_release",
    layout="homogeneous",
)
fpga.enumerate_grid()
fpga.render_layout(filename="_small_layout_ccff_fabric_render.svg", grid_io=True)

fabric_key = FabricKeyGenCCFF(fpga)
fabric_key.create_fabric_key()

fabric_key.render_svg(filename="_small_layout_ccff_fabric_render.svg")
fabric_key.save_fabric_key(filename="_serpentine_fabric_key.xml")
