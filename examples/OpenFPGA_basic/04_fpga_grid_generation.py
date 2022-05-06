"""
===========================
FPGA Layout grid generation
===========================

This class generates the 2D matrix of the FPGA grid.


**layout section of Architecture file**

.. rst-class:: hidden

.. program-output:: bash -c "mkdir -p auto_prog_output && xmllint --format --xpath '//layout' ../../examples/OpenFPGA_basic/support_files/vpr_arch_render_demo.xml > ./auto_prog_output/arch_layout_snnipet.xml"


.. literalinclude:: ../auto_prog_output/arch_layout_snnipet.xml
    :language: xml


**Expected Output**:

**_complete_fpga_grid**
This prints complete logic block grid, if the logic block has width or height larger than
a unit LB width it is represeted by arrows (left and top arrows only)

.. literalinclude:: ../../../examples/OpenFPGA_basic/_fpga_grid.txt

**_complete_grid_metrics**

.. literalinclude:: ../../../examples/OpenFPGA_basic/_complete_grid_metrics.txt

**_complete_metrics**

.. literalinclude:: ../../../examples/OpenFPGA_basic/_complete_metrics.txt


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
                       layout="dp")
    fpga.enumerate_grid()
    # Print CLB Grid
    output = fpga.print_grid()

    # grid_output
    with open("_fpga_grid.txt", "w") as fp:
        fp.write(output)

    # Complete Matrics
    with open("_complete_grid_metrics.txt", "w") as fp:
        for y in range(fpga.height-1, -1, -1):
            for x in range(fpga.width):
                fp.write("{0:^18}".format("[%s]" % " ".join(
                    map(str, fpga.get_block(x, y)))))
            fp.write("\n")

    # Complete metrics
    with open("_complete_metrics.txt", "w") as fp:
        for y in range(2*(fpga.height-1), -1, -1):
            for x in range((fpga.width*2)-1):
                fp.write(" {0:^12} ".format(fpga.get_top_instance(x, y)))
            fp.write("\n")


if __name__ == "__main__":
    main()
