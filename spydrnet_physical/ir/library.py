import logging
import typing

import spydrnet as sdn
from spydrnet.ir import Library as LibraryBase

logger = logging.getLogger('spydrnet_logs')


if typing.TYPE_CHECKING:
    from spydrnet.ir import Library as LibrarySDN
    from spydrnet_physical.ir.first_class_element import \
        FirstClassElement as FirstClassElementPhy
    LibraryBase = type(
        "DefinitionBase", (LibrarySDN, FirstClassElementPhy), {})


class Library(LibraryBase):

    def create_top_wrapper(self, name=None, inst_name=None, port_map=None):
        """ Creates 1-to-1 wrapper on top of current top_instance

        args:
            name (str): New top wrapper name (default: <top>_wrapper).
            inst_name (str): current top instance name (default: <top>_1).
            port_map (Callable): Function to return alternate name for port

        returns:
            (Definition): returns new wrapper definition
        """
        top_instance = self._netlist.top_instance
        name = name or f"{top_instance.name}_wrapper"
        inst_name = inst_name or f"{top_instance.reference.name}_1"
        port_map = port_map or (lambda x: x)
        new_def = self.create_definition(name)
        child_inst = new_def.create_child(inst_name,
                                          reference=top_instance.reference)

        for each_port in top_instance.reference.ports:
            new_port = each_port.clone()
            new_def.add_port(new_port)
            cable = new_def.create_cable(
                each_port.name, wires=each_port.size)
            cable.connect_instance_port(child_inst, next(
                top_instance.get_ports(each_port.name)))
            cable.connect_port(new_port)
            new_port.change_name(port_map(new_port.name))
        self._netlist.top_instance = sdn.Instance(name)
        self._netlist.top_instance.reference = new_def
        return new_def
