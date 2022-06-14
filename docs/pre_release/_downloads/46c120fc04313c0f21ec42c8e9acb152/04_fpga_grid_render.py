"""
==============================
RenderFPGA Pre Generation Grid
==============================

This class generates the 2D matrix of the FPGA grid.


**layout section of Architecture file**

.. image:: ../../../examples/OpenFPGA_basic/_small_layout_render.svg
   :width: 60%
   :align: center

.. image:: ../../../examples/OpenFPGA_basic/_ultimate_layout_render.svg
   :width: 90%
   :align: center

.. image:: ../../../examples/OpenFPGA_basic/_ultimate_layout_render_sized.svg
   :width: 90%
   :align: center

"""

import logging

import spydrnet as sdn
from spydrnet_physical.util import FPGAGridGen

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


def main():
    fpga = FPGAGridGen(design_name="example_design",
                       arch_file="./support_files/vpr_arch_render_demo.xml",
                       release_root="_release",
                       layout="small")
    fpga.enumerate_grid()

    dwg = fpga.render_layout(filename="_small_layout_render.svg", markers=True)

    # Demonstrates how tomodify the structure
    fpga = FPGAGridGen(design_name="example_design",
                       arch_file="./support_files/vpr_arch_render_demo.xml",
                       release_root="_release",
                       layout="ultimate")
    fpga.enumerate_grid()
    dwg = fpga.render_layout(
        filename="_ultimate_layout_render.svg", grid_io=True)

    fpga.get_instance("cbx_1__0_")["xlink:href"][1:]
    fpga.get_symbol_of_instance("cbx_1__0_")
    fpga.get_symbol("ram9k")
    fpga.add_style("symbol[id='ram9k'] * { fill:#a8dd00;}")
    print("-----")
    # Need Some more effforts
    fpga.merge_symbol(["cbx_1__0_", "clb_1__1_"], "new_symbol")
    dwg.save(pretty=True, indent=4)

    # Demonstrates how to modify the dimensions
    fpga = FPGAGridGen(design_name="example_design",
                       arch_file="./support_files/vpr_arch_render_demo.xml",
                       release_root="_release",
                       layout="ultimate")
    fpga.enumerate_grid()
    fpga.default_parameters["cbx"][0] = 10
    fpga.default_parameters["cby"][1] = 10
    dwg = fpga.render_layout(
        filename="_ultimate_layout_render_sized.svg", grid_io=True)


if __name__ == "__main__":
    main()
