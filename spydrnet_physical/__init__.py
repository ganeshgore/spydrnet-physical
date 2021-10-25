# pylint: skip-file
# Release data
import os
import glob
from spydrnet.parsers import parse
from spydrnet_physical import release

__author__ = '%s <%s>' % (release.authors['gore'])
__license__ = release.license

__date__ = release.date
__version__ = release.version
__release__ = release.release

base_dir = os.path.dirname(os.path.abspath(__file__))

example_netlist_names = list()
for filename in glob.glob(os.path.join(base_dir, 'support_files', 'sample_verilog', "*.v")):
    basename = os.path.basename(filename)
    example_netlist_names.append(basename[:basename.index('.')])
example_netlist_names.sort()

def load_netlist_by_name(name):
    assert name in example_netlist_names, "Example netlist not found"
    return parse(os.path.join(base_dir, 'support_files', 'sample_verilog', name + ".v"))
