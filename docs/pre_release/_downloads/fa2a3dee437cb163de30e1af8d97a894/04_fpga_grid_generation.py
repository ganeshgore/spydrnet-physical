"""
===========================
FPGA Layout grid generation
===========================

This class generates the 2D matrix of the FPGA grid.


**layout section of Architecture file**


.. program-output:: bash -c "xmllint --format --xpath '//layout' ../../examples/OpenFPGA/basic/support_files/vpr_arch_render_demo.xml > ./auto_prog_output/arch_layout_snnipet.xml"


.. literalinclude:: ../../auto_prog_output/arch_layout_snnipet.xml
   :language: xml


**Expected Output**:

.. code-block:: text

    EMPTY     io_top     io_top     io_top     io_top     io_top     io_top     EMPTY
    io_left     clb        clb        clb        clb        clb        clb      io_right
    io_left     clb        clb        clb        clb        clb        clb      io_right
    io_left    ram9k                 ram9k                 ram9k                io_right
    io_left     clb        clb        clb        clb        clb        clb      io_right
    io_left     dsp                   dsp                   dsp                 io_right
    io_left     clb        clb        clb        clb        clb        clb      io_right
    EMPTY   io_bottom  io_bottom  io_bottom  io_bottom  io_bottom  io_bottom    EMPTY


.. literalinclude:: ../../../../examples/OpenFPGA/basic/_complete_grid_metrics.txt


.. literalinclude:: ../../../../examples/OpenFPGA/basic/_complete_metrics.txt


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
    fpga.print_grid()

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
