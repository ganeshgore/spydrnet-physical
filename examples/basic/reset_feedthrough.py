"""
=====================================
Create Reset Feedthrough in fpga_top
=====================================

"""

import spydrnet as sdn
import spydrnet_physical as sdnphy

netlist = sdnphy.load_netlist_by_name('_fpga_top')
print(netlist)
top = netlist.top_instance

#Getting the ports' list for our reference
port_names=[]
ports = list(top.get_ports())
for i in range(len(ports)):
    port_names.append(ports[i].name)
print(port_names)

#Getting the cables' list for our reference
cables = list(top.get_cables())
cable_names=[]
for i in range(len(cables)):
    cable_names.append(cables[i].name)
print(cable_names)

#Creating feedthrough port for reset cable
top.reference.create_feedthroughs_ports(next(top.get_cables("rst_in")))

sdn.compose(netlist, '_reset_feedthrough1.v', skip_constraints=True)
_ref=[]
_ref_mod=[]

def get_module_list(current_instance,indentation="",level=0):
    if current_instance.reference.name not in _ref_mod:
        _ref.append(current_instance.name)
        _ref_mod.append(current_instance.reference.name)
    for child in current_instance.reference.children:
        get_module_list(child,indentation+"     ",level+1)

get_module_list(top)

instances_list=[]
for i in range(1,len(_ref)):
    instances_list.append(next(top.reference.get_instances(_ref[i])))

# print(_ref)
# print(ref_list)
# print(_ref_mod)

#Creating feedthrough in all the present modules 
top.reference.create_feedthrough(instances_list[0:len(instances_list)-1], next(top.reference.get_cables("rst_in")) )

def hierarchy(current_instance,indentation="",level=0):
    print(indentation,level,'',current_instance.name," --instance of",current_instance.reference.name,"--")
    for child in current_instance.reference.children:
        hierarchy(child,indentation+"     ",level+1)

hierarchy(top)
sdn.compose(netlist, '_reset_feedthrough1.v', skip_constraints=True)
