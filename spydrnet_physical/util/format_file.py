import spydrnet as sdn
import tempfile
import argparse
import os
import shutil
from spydrnet_physical.util.shell import launch_shell
from spydrnet_physical.util import get_names


def format_verilog():
    """
    Method called from the command line executable
    """
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--infile", type=str)
    parser.add_argument("-o", "--outfile", type=str)
    args = parser.parse_args()
    # print(args.infile, args.outfile)
    infile, outfile = args.infile, args.outfile

    # Read netlist and format
    netlist = sdn.parse(infile)
    netlist.name = "--"

    # Change assign definition instance names
    assign_lib = next(netlist.get_libraries("*SDN_VERILOG_ASSIGNMENT*"), None)
    if assign_lib:
        for instance in next(assign_lib.get_definitions()).references:
            try:
                input_wire = next(instance.get_port_pins("i")).wire
                output_wire = next(instance.get_port_pins("o")).wire
                instance_name = output_wire.cable.name + "__" + str(output_wire.index())
                instance.name = instance_name
            except StopIteration:
                launch_shell()

    dirname = os.path.dirname(infile)
    basename = os.path.basename(infile)
    outfile_default = os.path.join(dirname, f"_{basename}")
    sdn.compose(
        netlist,
        outfile_default,
        write_blackbox=False,
        skip_constraints=True,
        sort_all=True
    )
    if outfile:
        shutil.move(outfile_default, outfile)
    else:
        shutil.move(outfile_default, infile)


if __name__ == "__main__":
    format_verilog()
