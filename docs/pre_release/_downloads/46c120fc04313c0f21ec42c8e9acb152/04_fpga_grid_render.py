"""
==============================
RenderFPGA Pre Generation Grid
==============================

This example demonstrated how to perform design planning/ floorplanning
even before generating **OpenFPGA netlist**.

This rendering scheme is usefull to visualise global signal and
clock signal planning

.. note:: at this stage we dont have information of unique modules and its
   instances, hence during this rendering every instance is derived from same
   shapes


**Default FPGA grid generation**

.. image:: ../../../examples/OpenFPGA_basic/_small_layout_render.svg
   :width: 60%
   :align: center

"""

import logging

import spydrnet as sdn
from spydrnet_physical.util import FPGAGridGen

logger = logging.getLogger("spydrnet_logs")
sdn.enable_file_logging(LOG_LEVEL="INFO")


# %%
#
# **Create simple FPGA grid**
#
#
fpga = FPGAGridGen(
    design_name="example_design",
    arch_file="../support_files/vpr_arch_render_demo.xml",
    layout="small",
)
fpga.enumerate_grid()
dwg = fpga.render_layout(
    filename="_small_layout_render.svg", grid_io=True, markers=True)

# %%
# **Modify the dimensions**
# This example adds rectangular shape to all the modules in te design
#
# .. image:: ../../../examples/OpenFPGA_basic/_ultimate_layout_render.svg
#    :width: 60%
#    :align: center

fpga = FPGAGridGen(
    design_name="example_design",
    arch_file="../support_files/vpr_arch_render_demo.xml",
    layout="small",
)
fpga.enumerate_grid()
fpga.default_parameters["cbx"][0] = 10
fpga.default_parameters["cby"][1] = 10
dwg = fpga.render_layout(grid_io=False)
fpga.add_style("symbol[id='mcu'] * { fill:#ECCCB2;}")
dwg.saveas("_ultimate_layout_render.svg", pretty=True, indent=4)

# %%
# **Modify the structure**
#
# .. image:: ../../../examples/OpenFPGA_basic/_ultimate_layout_render_sized.svg
#    :width: 60%
#    :align: center

fpga.get_symbol_of_instance("cbx_1__2_")
fpga.get_symbol("mcu")
surrounding_routing = ["mcu_1__1_"]
surrounding_routing += ["cbx_1__2_", "sb_1__2_", "cbx_2__2_"]
surrounding_routing += ["cbx_1__0_", "sb_1__0_", "cbx_2__0_"]
fpga.merge_symbol(surrounding_routing, "new_mcu_module")

fpga.add_style(
    "symbol[id='new_mcu_module'] * { fill:#a8dd00; opacity: 0.5}")
dwg.saveas("_ultimate_layout_render_sized.svg", pretty=True, indent=4)
