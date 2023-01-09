"""
=====================================
Display Netlist Information Functions
=====================================

.. note:: This example is taken from SpyDrNet respository


Some example functions that can be run to display information in a netlist:
    1) print the hierarchy in a netlist
    2) print each library with its definitions in a netlist
    3) print connections between ports of each instance in a netlist
    4) print the number of times each primitive is instanced

Note: because the hierarchy function uses recursion, the maximum recursion depth may be exceeded if used for large designs

| For an even simpler display of netlist information, try using these functions with the Minimal Script example.

| Also, JensRestemeier (not affiliated with BYU CCL) created a tool to generate images of netlists. See his `github repository <https://github.com/JensRestemeier/EdifTests>`_.


**Output log**

.. literalinclude: ../../../examples/basic/_netlist_info_spydrnet.log

"""

import logging
import spydrnet as sdn
from spydrnet.util.selection import Selection

# print the hierarchy of a netlist

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO', filename="netlist_info")


def hierarchy(current_instance, indentation="", level=0):
    logger.info(" %s %d --instance of %s %s --", indentation, level,
                current_instance.name, current_instance.reference.name)
    for child in current_instance.reference.children:
        hierarchy(child, indentation+"     ", level+1)

# print a list of all libraries and definitions in a netlist


def libraries_definitions(my_netlist):
    for library in my_netlist.libraries:
        definitions = list(
            definition.name for definition in library.definitions)
        logger.info("DEFINITIONS IN '%s': %s", library.name, definitions)

# prints each instance and it's connections (what inputs to it and what it outputs to)


def print_connections(current_netlist):
    logger.info("CONNECTIONS:")
    for instance in current_netlist.get_instances():
        logger.info("Instance name: %s", instance.name)
        for out_going_pin in instance.get_pins(selection=Selection.OUTSIDE, filter=lambda x: x.inner_pin.port.direction is sdn.OUT):
            if out_going_pin.wire:
                next_instances = list(str(pin2.inner_pin.port.name + ' of ' + pin2.instance.name)
                                      for pin2 in out_going_pin.wire.get_pins(selection=Selection.OUTSIDE, filter=lambda x: x is not out_going_pin))
                logger.info('\t Port %s ----> %s',
                            out_going_pin.inner_pin.port.name, next_instances)
        for in_coming_pin in instance.get_pins(selection=Selection.OUTSIDE, filter=lambda x: x.inner_pin.port.direction is sdn.IN):
            if in_coming_pin.wire:
                previous_instances = list(pin2 for pin2 in in_coming_pin.wire.get_pins(
                    selection=Selection.OUTSIDE, filter=lambda x: x is not in_coming_pin))
                checked_previous_instances = list(str(x.inner_pin.port.name + ' of ' + x.instance.name) for x in previous_instances if (
                    x.inner_pin.port.direction is sdn.OUT or (x.inner_pin.port.direction is sdn.IN and not x.instance.is_leaf())) is True)
                logger.info('\t %s ----> Port %s', checked_previous_instances,
                            in_coming_pin.inner_pin.port.name)


def instance_count(current_netlist):
    logger.info("Number of times each primitive is instanced:")
    primitives_library = next(
        current_netlist.get_libraries("hdi_primitives"), None)
    for primitive in primitives_library.get_definitions():
        count = 0
        for instance in current_netlist.get_instances():
            if primitive.name == instance.reference.name:
                count += 1
        logger.info("\t %s : %s", primitive.name, count)


netlist = sdn.load_example_netlist_by_name("fourBitCounter")

logger.info("HIERARCHY:")
hierarchy(netlist.top_instance)
libraries_definitions(netlist)
print_connections(netlist)
instance_count(netlist)


# %%
#
# **Output log**
#
# .. literalinclude: ../../../examples/basic/_netlist_info_spydrnet.log
#
