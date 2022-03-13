"""
=====================================
Create Reset Feedthrough in fpga_top
=====================================

"""
import glob
import tempfile

import spydrnet as sdn
import spydrnet_physical as sdnphy
from spydrnet_physical.util import ConnectionPattern
from spydrnet_physical.util import OpenFPGA

netlist = sdnphy.load_netlist_by_name('_sample')

proj = "../homogeneous_fabric"
source_files = glob.glob(f'{proj}/*_Verilog/fpga_top.v')  
source_files += glob.glob(f'{proj}/*_Verilog/routing/*.v')
source_files += glob.glob(f'{proj}/*_Verilog/sub_module/*.v')
source_files += glob.glob(f'{proj}/*_Verilog/lb/*.v')

with tempfile.NamedTemporaryFile(suffix=".v") as fp:
    for eachV in source_files:
        with open(eachV, "r") as fpv:
            fp.write(str.encode(" ".join(fpv.readlines())))
    
    #Used only for our reference to check the verilog file 
    with open(fp.name) as firstfile, open('_sample.v','w') as secondfile:
        for line in firstfile:
            secondfile.write(line)
    fp.seek(0)
    netlist = sdn.parse(fp.name)

top = netlist.top_instance
top_definition = netlist.top_instance.reference
#Getting the ports' list for our reference
port_names=[]
ports = list(top.get_ports())
for i in range(len(ports)):
    port_names.append(ports[i].name)
# print(port_names)

#Getting the cables' list for our reference
cable_names=[]
cables = list(top.get_cables())
for i in range(len(cables)):
    cable_names.append(cables[i].name)
# print(cable_names)


_inst_list, _def_list = [], []
def get_inst_list(current_instance,indentation="",level=0):
    if current_instance.reference.name not in _def_list:
        _inst_list.append(current_instance.name)
        _def_list.append(current_instance.reference.name)
    for child in current_instance.reference.children:
        get_inst_list(child,indentation+"     ",level+1)

get_inst_list(top)

# print(_inst_list)
# print(_def_list)

p_manager = ConnectionPattern(9, 9)
fishbone_pattern = p_manager.get_fishbone()

#Assumption square Grid 9*9
grid_size=9
def get_reference(x, y):
    for X,Y in zip(range(0,grid_size), range(0,grid_size)):
        if   X%2 == 0 and Y%2 == 0:
            return next(netlist.get_instances(f"sb_{x}__{y}_")).reference.name
        elif X%2 == 0 and Y%2 != 0:
            return next(netlist.get_instances(f"cbx_{x}__{y}_")).reference.name
        elif X%2 != 0 and Y%2 == 0:
            return next(netlist.get_instances(f"cby_{x}__{y}_")).reference.name
        elif X%2 != 0 and Y%2 != 0:
            return next(netlist.get_instances(f"grid_clb_{x}__{y}_")).reference.name


def get_top_instance(x, y):
    for X,Y in zip(range(0,grid_size), range(0,grid_size)):
        if   X%2 == 0 and Y%2 == 0:
            return next(netlist.get_instances(f"sb_{x}__{y}_"))
        elif X%2 == 0 and Y%2 != 0:
            return next(netlist.get_instances(f"cbx_{x}__{y}_"))
        elif X%2 != 0 and Y%2 == 0:
            return next(netlist.get_instances(f"cby_{x}__{y}_"))
        elif X%2 != 0 and Y%2 != 0:
            return next(netlist.get_instances(f"grid_clb_{x}__{y}_"))


fishbone_pattern.get_reference = get_reference 
fishbone_pattern.get_top_instance = get_top_instance

rst_cable = top_definition.create_cable("rst_in", wires=1)

fishbone_pattern.create_ft_ports(netlist, "rst_in")
fishbone_pattern.create_ft_connection(top_definition, rst_cable)

def hierarchy(current_instance,indentation="",level=0):
    print(indentation,level,'',current_instance.name," --instance of",current_instance.reference.name,"--")
    for child in current_instance.reference.children:
        hierarchy(child,indentation+"     ",level+1)

# hierarchy(top)
sdn.compose(netlist, '_reset_feedthrough1.v', skip_constraints=True)
