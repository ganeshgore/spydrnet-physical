import spydrnet as sdn
import tempfile
import argparse
import os
import shutil


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
