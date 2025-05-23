import logging
import typing
from itertools import combinations

import numpy as np
import spydrnet as sdn
from spydrnet.ir import Definition as DefinitionBase
from spydrnet.ir.innerpin import InnerPin
from spydrnet.ir.outerpin import OuterPin
from spydrnet.ir.port import Port
from spydrnet_physical.global_state import global_callback as sdnphy_global_callback
from spydrnet_physical.ir.shaping_utils import shaping_utils

logger = logging.getLogger("spydrnet_logs")
try:
    import networkx as nx
except ImportError:
    logger.debug("Networks module not loaded")


if typing.TYPE_CHECKING:
    from spydrnet.ir import Definition as DefinitionSDN
    from spydrnet_physical.ir.first_class_element import (
        FirstClassElement as FirstClassElementPhy,
    )

    DefinitionBase = type("DefinitionBase", (DefinitionSDN, FirstClassElementPhy), {})


class Definition(DefinitionBase):
    """
    Extending the definitions representation
    """

    def __init__(self, name=None, properties=None):
        super().__init__(name=name, properties=properties)
        properties = properties or dict()
        # self.properties["WIDTH"] = properties.get("WIDTH", 50)
        # self.properties["HEIGHT"] = properties.get("WIDTH", 50)

    @property
    def utilization(self):
        """
        Return utilization of this module
        """
        if (float(self.properties.get("AREA_UM", 0)) > 0) and (self.area > 0):
            return self.properties.get("AREA_UM", 0) / self.area
        else:
            return -1

    @property
    def area(self):
        shape = self.data["VERILOG.InlineConstraints"].get("SHAPE", None)
        if shape == "cross":
            a, b, c, d, e, f = self.data["VERILOG.InlineConstraints"].get(
                "POINTS", [0, 0, 0, 0, 0, 0]
            )
            return ((a + f + c) * d) + ((b + d + e) * a) - (d * a)
        elif shape == "custom":
            return shaping_utils.PolyArea2D(
                shaping_utils.get_custom_boundary(
                    self.data["VERILOG.InlineConstraints"].get(
                        "POINTS", [0, 0, 0, 0, 0, 0]
                    )
                )
            )
        else:
            W = self.data["VERILOG.InlineConstraints"].get("WIDTH", 0)
            H = self.data["VERILOG.InlineConstraints"].get("HEIGHT", 0)
            return W * H

    def _disconnect_port(self, port):
        """
        This method disconnects the definition port from its cable
        This makes the port dangling, this method is used before
        removing the port
        """
        assert port in self._ports, "Port does not belong to this definition"
        for pin in port.pins:
            if pin.wire:
                pin.wire.disconnect_pin(pin)
            del pin

    def remove_cable(self, cable):
        """Remove a cable from the definition.

        The cable must be a member of the definition.

        parameters
        ----------

        cable - (Cable) the cable to be removed from the definition
        """
        assert cable.definition == self, "Cable is not included in definition"
        # Need to turn on this
        # for each_wire in cable.wires:
        #     for pins in each_wire.pins:
        #         each_wire.disconnect_pin(pins)
        self._remove_cable(cable)
        self._cables.remove(cable)

    def remove_port(self, port):
        """
        Remove port from the definition. (Overrides the base method)

        parameters
        ----------

        port: (Port) the port to be removed, must be of this definition
        """
        assert port.definition == self, "Port is not included in definition"
        self._remove_port(port)
        self._disconnect_port(port)
        for pin in port.pins:
            port.remove_pin(pin)
        self._ports.remove(port)

    def create_ft_ports(self, *args, **kwargs):
        """Alias to create_feedthroughs_ports"""
        return self.create_feedthroughs_ports(*args, **kwargs)

    def create_feedthroughs_ports(
        self, cable, suffix="ft", get_port_names=lambda x: None
    ):
        """
        Given the cable object it creates a feedthrough ports on this definition

        - The new ports names as {cable_name}_{suffix}_in and
          {cable_name}_{suffix}_out - Direct assignment is created
          beetween newly added two ports

        args:
            cable (Port): The cable for which feedthrough needs to be created
            suffix (str): Sufffix used for the port naming
            get_port_names(callable): function to return custom names
                             get_port_names(sdn.IN or sdn.out)

        Returns:
            tuple: Feedthrough port (inport and outport)
        """
        inport_name = get_port_names(sdn.IN) or f"{cable.name}_{suffix}_in"
        outport_name = get_port_names(sdn.OUT) or f"{cable.name}_{suffix}_out"
        inport, outport = (
            self.create_port(
                inport_name,
                pins=cable.size,
                is_scalar=cable.is_scalar,
                lower_index=cable.lower_index,
                direction=sdn.IN,
            ),
            self.create_port(
                outport_name,
                pins=cable.size,
                is_scalar=cable.is_scalar,
                lower_index=cable.lower_index,
                direction=sdn.OUT,
            ),
        )
        # Input port cable and output port cable
        int_c = self.create_cable(inport_name, wires=cable.size)
        out_c = self.create_cable(outport_name, wires=cable.size)

        assign_lib = self._get_assignment_library()
        assign_def = self._get_assignment_definition(assign_lib, cable.size)
        inst_name = f"{inport_name}_{outport_name}_ft"
        i = 1
        while next(self.get_instances(inst_name), None):
            inst_name = f"{inport_name}_{outport_name}_ft" + f"_{i}"
            i += 1

        instance = self.create_child(inst_name, reference=assign_def)

        int_c.connect_port(inport)
        int_c.connect_instance_port(instance, next(assign_def.get_ports("i")))
        out_c.connect_port(outport)
        out_c.connect_instance_port(instance, next(assign_def.get_ports("o")))
        return (inport, outport)

    # TODO: Creates problem when cable is output port cable
    def create_feedthrough(
        self,
        instances_list,
        cable,
        get_port_names=lambda port_dir: None,
        get_cable_names=lambda indx, inst: None,
    ):
        """
        Creates a feedthrough for a single cable passing through
        list of instances

        The driver cable name is unchanged and newly created feedthrough cable
        name {cable_name}_ft_{indx}

        args:
            instances_list (list[instance]): List of instances to create
                                            feedthrough from
            cable (Cable): cable fro which feedthrough needs to be creared
            get_port_names(callable): --
            get_cable_names(callable): --

        Returns:
            list(Cable): List of newly created cables in order
        """
        if isinstance(instances_list, sdn.Instance):
            instances_list = (instances_list,)
        assert isinstance(cable, sdn.Cable), "Cable object required"
        assert (
            cable.definition == self
        ), "Cable {cable.name} does not belog to this definition"
        assert all(
            inst in self._children for inst in instances_list
        ), "Found inst which does not belong to this definition"

        cable_list = []
        for indx, instance in enumerate(instances_list):
            inport, outport = instance.reference.create_ft_ports(
                cable, get_port_names=get_port_names
            )

            cable_name = get_cable_names(indx, instance) or f"{cable.name}_ft_in_{indx}"
            new_cable = self.create_cable(cable_name, wires=cable.size)
            new_cable.connect_instance_port(instance, outport)

            for indx, each_w in enumerate(cable.wires):
                for pin in set(each_w.pins):
                    # These are loads and
                    if (
                        isinstance(pin, OuterPin) and (pin.port.direction == sdn.IN)
                    ) or (
                        isinstance(pin, InnerPin) and (pin.port.direction == sdn.OUT)
                    ):
                        each_w.disconnect_pin(pin)
                        new_cable.wires[indx].connect_pin(pin)
            cable.connect_instance_port(instance, inport)
            cable_list.append(new_cable)
        return cable_list

    def create_parallel_feedthrough(self, instances_list):
        # Same instances in each group
        assert len(set((len(inst) for _, inst in instances_list))) == 1

        # Create ports
        ft_port_seq = []
        for definition in set(inst.reference for inst in instances_list[0][1]):
            ft_port_seq.append(
                definition.create_feedthroughs_ports(instances_list[0][0], suffix="ft")
            )

        # Create connection between instances
        for cable, inst_list in instances_list:
            # disconnect and store load pins
            port_type = {
                pin.port.direction
                for wire in cable._wires
                for pin in wire.pins
                if isinstance(pin, InnerPin)
            }
            is_port_cable = bool(sdn.OUT in port_type)
            store_load_pins = []
            for wire in cable.wires:
                store_load_pins.append(tuple(wire.loads()))
                for pin in list(wire.loads()):
                    wire.disconnect_pin(pin)

            cable.connect_instance_port(inst_list[0], ft_port_seq[0][0])
            for indx, inst in enumerate(inst_list):
                new_cable = cable.clone()
                if is_port_cable:
                    cable.name = f"{inst.name}_{cable.name}"
                else:
                    new_cable.name = f"{inst.name}_{cable.name}"
                self.add_cable(new_cable)
                new_cable.connect_instance_port(inst, ft_port_seq[indx][1])

            for indx, wire in enumerate(new_cable.wires):
                for pin in store_load_pins[indx]:
                    wire.connect_pin(pin)

        return new_cable

    def create_ft_multiple(self, *args, **kwargs):
        """Alias to create_feedthrough_multiple"""
        return self.create_feedthrough_multiple(*args, **kwargs)

    def create_feedthrough_multiple(self, instances_list):
        """
        This creates feedthough from list of instances on multiple locations
        Expects the list of tuples in following format

        parameters
        ----------

        instances_list: (Cable, (inst1, inst1, . . . .instn)
        """
        cable, inst_tuple = instances_list
        # Check if first item is Cable
        assert isinstance(cable, sdn.Cable), "Cable object required"
        # Check if cable belognt to the same definition
        assert (
            cable.definition == self
        ), "Cable {cable.name} does not belog to thos definition"
        # Compare instance list is from same reference
        for instance in inst_tuple:
            assert isinstance(
                instance, sdn.Instance
            ), "Found {type(instance) in the instances list}"

        for definition in set(inst.reference for inst in inst_tuple):
            definition.create_feedthroughs_ports(cable, suffix="ft")

        for indx, each_inst in enumerate(inst_tuple):
            cable_name = f"{cable.name}_{each_inst.name}_ft"

            if indx == 0:
                port = next(each_inst.get_ports(f"{cable.name}_ft_in"))
                cable.connect_instance_port(each_inst, port)
            else:
                new_cable = self.create_cable(cable_name, wires=cable.size)
                outport = next(inst_tuple[indx - 1].get_ports(f"{cable.name}_ft_out"))
                inport = next(each_inst.get_ports(f"{cable.name}_ft_in"))
                new_cable.connect_instance_port(inst_tuple[indx - 1], outport)
                new_cable.connect_instance_port(each_inst, inport)

            if indx == len(inst_tuple) - 1:
                cable_name = f"{cable.name}_out"
                new_cable = self.create_cable(cable_name, wires=cable.size)
                outport = next(each_inst.get_ports(f"{cable.name}_ft_out"))
                new_cable.connect_instance_port(each_inst, outport)

        for indx, wire in enumerate(cable.wires):
            for eachpin in wire.loads():
                eachpin.wire.disconnect_pin(eachpin)
                new_cable.wires[indx].connect_pin(eachpin)

    def merge_multiple_instance(
        self, instances_list_tuple, new_definition_name=None, pin_map=None
    ):
        """
        This method can merge multiple group of instances
        having same order of reference definition.

        First pair of the instances_list_tuple is used to create new definition
        and that is reused while grouping remaining group of instances

        args:
            instances_list_tuple = [(inst_1, inst_2, ...., inst_n), <instance_name>]
            new_definition_name (str) = Name for the new definition
            pin_map (Callable)          = Function of dictionary to rename pins
        """
        main_def = None
        instance_list = []
        for instances_list, instance_name in instances_list_tuple:
            new_def, new_inst, _ = self.merge_instance(
                instances_list,
                new_definition_name=f"{new_definition_name}_{instance_name}",
                new_instance_name=instance_name,
                pin_map=pin_map,
            )
            instance_list.append(new_inst)
            if not main_def:
                # If this is first merge copy the newly created definition
                main_def = new_def
                main_def.name = new_definition_name
            else:
                new_inst.reference = main_def
                self.library.remove_definition(new_def)
        return main_def, instance_list

    @staticmethod
    def _call_merged_instance(new_mod, new_instance, instances_list):
        # def_data = instances_list[0].data["VERILOG.InlineConstraints"]
        # if def_data:
        outline = []
        new_mod.properties["AREA"] = 0
        new_mod.properties["AREA_UM"] = 0
        for each in instances_list:
            shape = each.reference.properties.get("SHAPE", None)
            if shape == "rect":
                outline.extend(shaping_utils._convert_rect_to_pt(each))
            if shape == "cross":
                outline.extend(shaping_utils._convert_cross_to_pt(each))
            new_mod.properties["AREA"] += each.reference.properties.get("AREA", 0)
            new_mod.properties["AREA_UM"] += each.reference.properties.get("AREA_UM", 0)
        LOC_X = min([each.properties.get("LOC_X", 0) for each in instances_list] or [0])
        LOC_Y = min([each.properties.get("LOC_Y", 0) for each in instances_list] or [0])
        new_instance.properties["LOC_X"] = LOC_X
        new_instance.properties["LOC_Y"] = LOC_Y
        if outline:
            shape, points = shaping_utils.get_shapes_outline(outline)
            new_instance.reference.properties["SHAPE"] = shape
            if shape == "cross":
                new_instance.reference.properties["POINTS"] = points
            if shape == "custom":
                new_instance.reference.properties["POINTS"] = (
                    shaping_utils.points_to_path(points)
                )
            if shape == "rect":
                new_instance.reference.properties["WIDTH"] = points[0]
                new_instance.reference.properties["HEIGHT"] = points[1]
            shaping_utils._interpret_custom_to_shape(new_instance.reference)

            logger.debug(
                f"{new_instance.name} "
                + f"[{new_instance.reference.name:15}]"
                + f"[{new_instance.reference.properties.get('SHAPE', 50):15}]"
                + f"[{new_instance.reference.properties.get('WIDTH', 50):15}]"
                + f" {shape} {points}"
            )

    # TODO: Try to break this method
    def merge_instance(
        self, instances_list, new_definition_name="", new_instance_name="", pin_map=None
    ):
        """
        Merges the list of instances to unique definition

        args:
            instances_list (List(Instance)): List of instances to be merged
            new_definition_name : Name of the new definition created
            new_instance_name   : Name of the new instance created
            pin_map (Callable, Dict) : External function to map new pin name
                    based in definition and instance name
                    get_pin_name(<definition_name:<str>, <pin_name:<str>,
                    <instance_name:<str>)

        returns:
            (Definition, Instance, Dict)
        """
        rename_map = {}  # Stores the final rename map

        # ====== Input Sanity checks
        for i, each_module in enumerate(instances_list):
            assert isinstance(each_module, sdn.Instance), (
                "Modulelist contains none non-intance object "
                + "[%s] at location %d " % (type(each_module), i)
            )

        if pin_map:
            if isinstance(pin_map, dict):
                pin_map_copy = pin_map

                def pin_map(x, y, _):
                    return pin_map_copy.get(x, {}).get(y, {})

            if not callable(pin_map):
                print(
                    "pin_map argument should be dictionary or function, "
                    + f"received {type(pin_map)}"
                )

        # ====== Create a new definition
        if not new_definition_name:
            new_def_name = (
                "_".join([each.reference.name for each in instances_list]) + "_merged"
            )
            print(f"Inferred definition name {new_def_name} ")
        else:
            new_def_name = new_definition_name
        new_mod = self.library.create_definition(name=new_def_name)

        # ===== Create instance of the definition
        if not new_instance_name:
            new_instance_name = f"{new_def_name}_1"
        merged_module = self.create_child(name=new_instance_name, reference=new_mod)

        # ===== Interate over each module and create new module
        for index, eachM in enumerate(instances_list):
            rename_map[eachM.reference.name] = {}
            rename_map[eachM.reference.name][index] = {}
            currMap = rename_map[eachM.reference.name][index]
            IntInst = new_mod.create_child(name=eachM.name, reference=eachM.reference)
            # Iterate over each port of current instance
            for p in eachM.get_ports():
                pClone = p.clone()  # It copied all pins, wires and cables
                for eachSuffix in [""] + [f"_{i}" for i in range(1000)]:
                    newName = pClone.name + eachSuffix
                    if not len(list(new_mod.get_ports(newName))):
                        break
                newCable = new_mod.create_cable(
                    name=newName,
                    is_downto=pClone.is_downto,
                    is_scalar=pClone.is_scalar,
                    lower_index=pClone.lower_index,
                )

                # Create connection inside new definition
                pClone = p.clone()  # It copied all pins, wires and cables
                tmp_pins = p.pins if pClone.is_downto else p.pins[::-1]
                for eachPClone, eachP in zip(pClone.pins, tmp_pins):
                    w = newCable.create_wire()
                    w.connect_pin(eachPClone)
                    w.connect_pin(IntInst.pins[eachP])
                pClone.change_name(newName)
                new_mod.add_port(pClone)

                currMap[p.name] = newName

                for eachPin in p.pins:
                    inst_out_pin = eachM.pins[eachPin]
                    conWire = inst_out_pin.wire
                    instPin = merged_module.pins[pClone.pins[eachPin.index()]]
                    if conWire:
                        conWire.connect_pin(instPin)
                        conWire.disconnect_pin(inst_out_pin)
                    newCable.wires[eachPin.index()].connect_pin(inst_out_pin)

            self.remove_child(eachM)
        sdnphy_global_callback._call_merged_instance(
            new_mod, merged_module, instances_list
        )
        self._call_merged_instance(new_mod, merged_module, instances_list)
        return new_mod, merged_module, rename_map

    def OptPins(
        self,
        pins=lambda x: True,
        dry_run=False,
        merge=True,
        absorb=True,
        remove_unconn=False,
    ):
        """
        This method optimizes the definitions pins bu inspecting all the
        instances of the definition

        parameters
        ----------

        dry_run: Just performs the dryrun and list the pins which can be merged or absorbed
        pins: only consider specific pins, provide filter function
        absorb: if two pins are only connected to each other they will be absorbed and internal connection will be made
        merge: if two pins are connected to each other and few other instances, one of the pin will be absorbed and other will exist
        remove_unconn: Remove unconnected pins
        """
        duplicatePins = []  # Set of all pins which can be merged or absorbed
        absorbPins = []  # Subset of duplicate pins
        unused_ports = []  # Subset of duplicate pins
        defPort = list([x for x in self.get_ports() if pins(x.name)])

        # Iterate over all the ports pairs of the definition
        for fromPort, toPort in combinations(defPort, 2):
            if len(fromPort.pins) == len(toPort.pins):
                # Compare only when port has same width
                sameNet = True  # Flag to detect boh ports are connected to same cable
                singleWire = True
                for eachPin1, eachPin2 in zip(fromPort.pins, toPort.pins):
                    for eachInst in self.references:
                        eachPin1 = eachInst.pins[eachPin1]
                        eachPin2 = eachInst.pins[eachPin2]
                        if (eachPin1.wire is None) or (eachPin2.wire is None):
                            sameNet = False
                            break
                        elif not (eachPin1.wire == eachPin2.wire):
                            sameNet = False
                            break
                        elif singleWire:
                            if eachPin1.wire:
                                singleWire = set(eachPin1.wire.pins) == set(
                                    (eachPin1, eachPin2)
                                )
                            else:
                                singleWire = False

                if sameNet:
                    # Check if frompin exist in the previous pairs
                    already_paired = next(
                        (
                            dupliPins
                            for dupliPins in duplicatePins
                            if fromPort in dupliPins
                        ),
                        None,
                    )
                    if already_paired:
                        if not toPort in already_paired:
                            already_paired.append(toPort)
                    else:
                        portPair = [fromPort, toPort]
                        duplicatePins.append(portPair)
                    if singleWire:
                        absorbPins.append(portPair)
        if remove_unconn:
            for ports in defPort:
                is_wired = False
                for eachInst in self.references:
                    if not all(
                        [(eachInst.pins[pin].wire is None) for pin in ports.pins]
                    ):
                        is_wired = True
                        break
                if not is_wired:
                    unused_ports.append(ports)

        if not dry_run:
            for ports in duplicatePins[::-1]:
                ports.sort(key=lambda x: {sdn.IN: "1", sdn.OUT: "0"}[x.direction])
                for eachP1Pin in ports[0].pins:
                    ww = eachP1Pin.wire
                    for eachPort in ports[1:]:
                        # Remove all internal connection
                        wwP2 = eachPort.pins[eachP1Pin.index()].wire
                        for eachPin in wwP2.pins:
                            if isinstance(eachPin, sdn.OuterPin):
                                eachPin.wire.disconnect_pin(eachPin)
                                # Selects pins connected to the instance
                                ww.connect_pin(eachPin)

                for eachPort in ports[1:]:
                    self.remove_cable(eachPort.pins[0].wire.cable)
                    self.remove_port(eachPort)
                    logger.debug(f"Merged Ports {ports[0].name}<-{eachPort.name}")
                if ports in absorbPins:
                    self.remove_port(ports[0])
                    logger.debug(f"Absorbed port {ports[0].name}")
            if remove_unconn:
                for eachPort in unused_ports:
                    self.remove_port(eachPort)

        return duplicatePins if merge else absorbPins if absorb else None

    # TODO : Need to consider floating paraters
    def OptWires(self, no_load=True, no_driver=False, floating=True):
        """
        List the wires which can be optimised based on different constraints

        parameters
        ----------

        no_load: (bool) (Default: True) Wires without load pin
        no_driver: (bool) (Default: False) Wires without drivers pin
        floating: (bool) (Default: True) Wires without any connection to pin
        """
        for cable in self.get_cables():
            for wire in cable.wires:
                if len(wire.pins) < 2:
                    print(f"{wire} Wire an be trimmed ")

    # def OptInstances(self, checkInputs=True, checkOutputs=True):
    #     '''
    #     '''
    #     for c in self.children:
    #         for p in c.pins.values():
    #             # if (p.port.direction == Port.Direction.IN) and not checkInputs:
    #             #     continue
    #             # if (p.port.direction == Port.Direction.OUT) and not checkOutputs:
    #             #     continue
    #             if p.wire:
    #                 break
    #         else:
    #             print(f"{p._instance} Instance an be trimmed ")

    def _get_assignment_library(self):
        """
        Returns assignment library from the netlist of this definition.
        If the assignment library is missing it will create new and return
        """
        assert self.library, "Library is not defined for the definition"
        assert self.library.netlist, "netlist is not defined for the library definition"
        netlist = self.library.netlist
        assign_library = next(netlist.get_libraries("SDN_VERILOG_ASSIGNMENT"), None)
        if assign_library is None:
            logger.info("Missing SDN_VERILOG_ASSIGNMENT libarary Creating new")
            assign_library = netlist.create_library(name="SDN_VERILOG_ASSIGNMENT")
        return assign_library

    def _get_assignment_definition(self, assign_library, size):
        """
        Returns assignment definition for the give size

        parameters
        ----------

        assign_library = ``SDN_VERILOG_ASSIGNMENT`` library
        size = (int) Size of the assignment block
        """
        assign_def_name = f"SDN_VERILOG_ASSIGNMENT_{size}"
        definition = next(assign_library.get_definitions(assign_def_name), None)
        if definition is None:
            definition = assign_library.create_definition(name=assign_def_name)
            p_in = definition.create_port("i", pins=size)
            p_out = definition.create_port("o", pins=size)
            p_in.direction = p_in.Direction.IN
            p_out.direction = p_out.Direction.OUT
            cable = definition.create_cable("through", wires=size)
            cable.connect_port(p_in)
            cable.connect_port(p_out)
        return definition

    def duplicate_port(self, port, port_name=None):
        """
        Duplicates existing port in the definition
        Uses assign block beetween to short two cables
        If post in output port ``assign new_port = initial_port``
        else ``assign initial_port = new_port``

        parameters
        ----------

        port: (Port) Port of this definition
        port_name: (str) Options New port name (default {port_name}_dup)
        """
        assert isinstance(port, sdn.Port), f"Required Port but found {type(port)}"

        assert self.library, "Library is not defined for the definition"
        assert self.library.netlist, "netlist is not defined for the library definition"

        new_port_name = port_name if port_name else f"{port.name}_dup"
        new_port = self.create_port(
            new_port_name,
            direction=port.direction,
            is_scalar=port.is_scalar,
            lower_index=port.lower_index,
            is_downto=port.is_downto,
        )
        new_port.create_pins(port.size)
        new_cable = self.create_cable(
            new_port_name,
            is_scalar=port.is_scalar,
            lower_index=port.lower_index,
            is_downto=port.is_downto,
            wires=port.size,
        )
        port_cable = port.pins[0].wire.cable

        assign_library = self._get_assignment_library()
        definition = self._get_assignment_definition(assign_library, new_cable.size)

        instance = self.create_child(
            f"SDN_ASSIGNMENT_{port.name}_{new_port.name}", reference=definition
        )
        if port.is_output:
            port_cable.connect_instance_port(instance, next(definition.get_ports("i")))
            new_cable.connect_instance_port(instance, next(definition.get_ports("o")))
        else:
            new_cable.connect_instance_port(instance, next(definition.get_ports("i")))
            port_cable.connect_instance_port(instance, next(definition.get_ports("o")))
        return new_port

    def combine_cables(self, new_cable_name, cables, quiet=False):
        """
        Combines multiple cables to new cable.
        Helpful in creating Bus/Vector from scalar wires

        parameters
        ----------

        new_cable_name: (str) New cable name
        cables: (list[Cable]) List of cables
        quiet: (bool) Do not raise error if no cables are passed
        """
        if len(cables) == 0:
            if quiet:
                return None
            else:
                assert False, "No cables provided"

        for c in cables[1:]:
            assert isinstance(
                c, sdn.Cable
            ), f"combine_cables can combine only cable found {type(c)}"
            assert (
                self == c.definition
            ), f"all ports to combine should belong to same definition"
            assert cables.count(c) == 1, f"Cable defined multiple times {c.name}"

        newCable = self.create_cable(new_cable_name, is_scalar=False)
        for c in cables[::-1]:
            for wire in c.wires[::-1]:
                c.remove_wire(wire)
                newCable.add_wire(wire)
            self.remove_cable(c)
        return newCable

    def combine_ports(self, port_name, ports, is_downto=False):
        """
        This method can combine multiple input or output ports togther
        to create a bus structure.

        It does create a cable for internal wires, but does not
        change anything about the external wire connection
        ports[0] will be newport[0]
        default properties will be used for creating a new port

        args:
            port_name (str) : Name of the new port
            ports (list[Ports]) : List of ports to combine

        return:
            (new_port, new_cable) : return new port and internal cable
        """
        direction = ports[0].direction
        for p in ports[1:]:
            assert isinstance(
                p, Port
            ), f"combine_ports can combine Ports found {type(p)}"
            assert (
                direction == p.direction
            ), f"combine_ports combines only input or output ports, \
                found {type(p.direction)}"
            assert (
                self == p.definition
            ), f"all ports to combine should belong to same definition"

        new_port = self.create_port(port_name, direction=direction, is_downto=is_downto)
        new_cable = self.create_cable(
            port_name, is_scalar=new_port.is_scalar, is_downto=is_downto
        )
        port_list = []
        for p in ports:
            port_list.append(p.name)
            newPin = new_port.create_pin()
            pp = p.pins[0]
            ppWire = pp.wire
            # Switch Instances connection
            for instance in self.references:
                if instance.pins[pp].is_connected:
                    instance.pins[pp].wire.connect_pin(instance.pins[newPin])
            if ppWire:
                # Switch Internal Wire
                ppWire.connect_pin(newPin)
                self.remove_cable(ppWire.cable)
                ppWire.cable.remove_wire(ppWire)
                new_cable.add_wire(ppWire)
            logger.debug(f"Removing port {p.name}")
            self.remove_port(p)
        logger.debug(
            f"Combined with {new_port.name} " + f"created cable {new_cable.name}"
        )
        logger.debug(f"{new_port.name} <- {port_list}")
        return new_port, new_cable

    def split_port_fanout(self, port, port_names=None):
        """
        Split the given port into multiple ports
        This is used to split the fanout ports
        """
        if isinstance(port, str):
            port = next(self.get_ports(port))

        port_names = port_names or (lambda args: f"{args[0]}_{args[1]}")

        instances = list(r for r in self.references if r.parent)
        assert (
            len(instances) == 1
        ), "Fanout split is only supported for single instance found %s" % "-".join(
            r.parent.name for r in self.references if r.parent
        )

        cable = next(self.get_cables(port.name))
        in_wire = instances[0].pins[port.pins[0]].wire

        for indx, pin in enumerate(list(cable.wires[0].pins)):
            if isinstance(pin, sdn.OuterPin):
                new_port_name = port_names((port.name, indx))
                new_port = self.create_port(new_port_name, direction=sdn.IN, pins=1)
                new_cable = self.create_cable(new_port_name, wires=1)
                new_cable.wires[0].connect_pin(new_port.pins[0])
                pin.wire.disconnect_pin(pin)
                new_cable.wires[0].connect_pin(pin)
                in_wire.connect_pin(instances[0].pins[new_port.pins[0]])

        self.remove_port(port)
        self.remove_cable(cable)

    def create_unconn_wires(self):
        unconn_cable = self.create_cable("unconn")
        w = unconn_cable.create_wire()  # dummy wire
        for instance in self.children:
            for pin in instance.get_port_pins(instance.reference.ports):
                if not pin.wire:
                    w = unconn_cable.create_wire()
                    w.connect_pin(pin)

    def merge_ports(self, new_port_name, port_sequence, reverse=False):
        new_port = self.create_port(new_port_name)
        new_cable = self.create_cable(new_port_name)

        for port in list(port_sequence):
            for pin in list(port.pins)[::-1]:
                wire = pin.wire
                port._pins.remove(pin)
                pin._port = None
                new_port.add_pin(pin)

                wire._cable = None
                new_cable.add_wire(wire)
            self.remove_cable(next(self.get_cables(port.name)))
            self.remove_port(port)
            new_port.direction = port.direction

        return new_port

    def split_port(self, port):
        """
        Split the given port

        Args:
            port (Port): Definition port to split into independent pins
        """
        if isinstance(port, str):
            port = next(self.get_ports(port))

        cable = next(self.get_cables(port.name))
        for indx, pin in enumerate(port.pins[::-1]):
            new_port = self.create_port(f"{port.name}_{indx}", direction=port.direction)
            new_cable = self.create_cable(f"{port.name}_{indx}")
            cable.remove_wire(pin.wire)
            new_cable.add_wire(pin.wire)
            pin._port = None
            port._pins.remove(pin)
            new_port.add_pin(pin)

        self.remove_port(port)
        self.remove_cable(cable)

    def flatten_instance(self, instance):
        """Flatterns single instance in the given definition"""
        assert isinstance(instance, sdn.Instance), "Argument not a Instance"
        assert instance in self.children, "Instance is not part of current definition"
        cable_map = {}
        # recreating internal cables on top level
        for cable in instance.reference.get_cables():
            if not cable.is_port_cable:
                new_cable = cable.clone()
                new_cable.name = instance.name + "_" + new_cable.name
                self.add_cable(new_cable)
                cable_map[cable] = new_cable
        # recreating sub instance on the top level and create connections
        for sub_instance in instance.reference.children:
            new_instance = sub_instance.clone()
            new_instance.name = instance.name + "_" + new_instance.name
            self.add_child(new_instance)
            # create connection, iteratre over each port of sub-instance
            for port in sub_instance.reference.ports:
                for pin in sub_instance.get_port_pins(port.name):
                    if not pin.wire:
                        # skip if sub-instance pin is not connected
                        continue
                    if pin.wire.cable.is_port_cable:
                        # if the pin wire is connected to instance port
                        pin_top = next(
                            filter(lambda x: isinstance(x, sdn.InnerPin), pin.wire.pins)
                        )
                        pin_top = instance.pins[pin_top]
                        if not pin_top.wire:
                            # skip if instance pin is not connected
                            continue
                        wire = pin_top.wire
                    else:
                        # internal wire
                        wire = cable_map[pin.wire.cable].wires[pin.wire.index()]
                    wire.connect_pin(new_instance.pins[pin])
        self.remove_child(instance)

    def get_connectivity_network(self, get_weights=None, split_ports=False):
        """
        This method converts current module into networkx graph
        each cell is represented as as node and nets are represented as edges

        - Netowrkx should be installed
        - Higher fanout nets are represented with independent edge from driver
        to each load

        """
        assert "nx" not in dir(), "Netowrkx library not installed"

        get_weights = get_weights or (lambda x: 1)

        def get_node_name(pin):
            if isinstance(pin, sdn.OuterPin):
                return pin.instance.name
            else:
                if split_ports and (pin.port.size > 1):
                    return f"{pin.port.name}_{pin.get_verilog_index}"
                else:
                    return pin.port.name

        # Variables
        graph = nx.DiGraph()
        node_map = {}
        edges = []
        elabel = []

        # Create Port Nodes first
        node_indx = 0
        logger.debug(f"Found {len(self.ports)} ports")
        for port in self.ports:
            for pin in port.pins:
                name = get_node_name(pin)
                graph.add_node(
                    node_indx,
                    label=name,
                    weight=get_weights(pin),
                    shape="rect",
                    port=True,
                    node_name=port.name,
                )
                node_map[name] = node_indx
                node_indx += 1
                if not split_ports:
                    break

        # Create Instances Nodes
        logger.debug(f"Found {len(self.children)} instances")
        for instance in self.children:
            name = instance.name
            graph.add_node(
                node_indx,
                port=False,
                weight=get_weights(instance),
                node_name=instance.name,
                label=instance.name,
            )
            node_map[instance.name] = node_indx
            node_indx += 1

        # Create edges
        logger.debug(f"Found {len(list(self.get_cables()))} nets")
        for cable in list(self.get_cables()):
            for wire in cable.wires:
                # Skip adding edge if there is no driver
                if not wire.get_driver():
                    logger.debug(f"No driver found for {cable.name}")
                    continue
                # Get driver [source node]
                # TODO: Consider multiple dirvers here
                driver_inst = get_node_name(wire.get_driver()[0])

                # Make connection from drivers to each load
                for p in wire.pins:
                    node = get_node_name(p)
                    if node == driver_inst:
                        continue
                    edges.append((node_map[driver_inst], node_map[node]))
                    elabel.append(f"{cable.name}_{wire.get_verilog_index}")

        logger.debug(f"Adding {len(set(edges))} edges")
        for edge in set(edges):
            weight = edges.count(edge)
            edge_name = elabel[edges.index(edge)]
            graph.add_edge(
                *edge, label=f"[{weight}]", edge_name=edge_name, weight=float(weight)
            )
        return graph

    def _remove_child(self, child):
        """
        Internal function for dissociating a child instance from the definition.
        """
        super()._remove_child(child=child)
        for pin in list(child.get_port_pins(child.get_ports())):
            if pin.wire:
                pin.wire.disconnect_pin(pin)

    def make_instance_unique(self, instance, new_name, instance_list=()):
        """clone the definition and point the reference to the new definition"""
        assert instance in self.children, "Isntance is not part of this definition"
        reference = instance.reference
        lib = instance.reference.library
        index = lib.definitions.index(reference)
        new_def = instance.reference.clone()
        if instance.reference.name is not None:
            name = instance.reference.name
            new_def.name = new_name or (name + "_new")
        lib.add_definition(new_def, index + 1)
        instance.reference = new_def
        for each in instance_list:
            try:
                next(self.get_instances(each)).reference = new_def
            except StopIteration:
                logger.exception("%s instance not found during uniquifying", each)
        return new_def

    def add_buffer(
        self, wire, buffer, instance_name, ports=("A", "Y"), new_cable_name=None
    ):
        """
        Adds buffer on the given net
        args:
            wire (sdn.Wire, sdn.Cable): Cable or a wire to be buffered
            buffer (str):
            instance_name (sdn.Instance):
            ports tuple(str, str):
        """
        pre_buffer_w = new_cable_name or f"{instance_name}_pre_buffer"

        if isinstance(wire, sdn.Cable):
            for each_wire in wire.wires:
                self.add_buffer(each_wire, buffer, instance_name, ports)
            return

        # Instantiate buffer
        buffer = (
            next(self.get_definitions(buffer)) if isinstance(buffer, str) else buffer
        )
        buffer_inst = self.create_child(name=instance_name, reference=buffer)
        a_pin = next(buffer_inst.get_port_pins(ports[0]))
        y_pin = next(buffer_inst.get_port_pins(ports[1]))

        if wire.cable.is_port_cable:
            driver_pin = list(
                filter(lambda x: isinstance(x, sdn.InnerPin), wire.cable.wires[0].pins)
            )[0]
            if driver_pin.port.direction == sdn.IN:
                # if buffering input net
                load_pins = list(
                    wire.get_pins(
                        selection="OUTSIDE",
                        filter=lambda x: (x.inner_pin.port.direction == sdn.IN)
                        and (x.instance.parent == self),
                    )
                )
                post_buffer_w = new_cable_name or f"{instance_name}_post_buffer"
                buffer_input_wire = self.create_cable(post_buffer_w, wires=1).wires[0]
                for pin in load_pins:
                    if pin.wire:
                        pin.wire.disconnect_pin(pin)
                        buffer_input_wire.connect_pin(pin)
                buffer_input_wire.connect_pin(y_pin)
                wire.connect_pin(a_pin)
                logger.debug(
                    "Added buffer in %s with instance name %s",
                    self.name,
                    buffer_inst.name,
                )
                return
                # raise NotImplementedError("Buffer on input net is not supported")
        driver_pin = next(
            wire.get_pins(
                selection="OUTSIDE",
                filter=lambda x: x.inner_pin.port.direction == sdn.OUT,
            )
        )
        driver_pin.wire.disconnect_pin(driver_pin)

        buffer_input_wire = self.create_cable(pre_buffer_w, wires=1).wires[0]
        buffer_input_wire.connect_pin(driver_pin)
        buffer_input_wire.connect_pin(a_pin)
        wire.connect_pin(y_pin)
        logger.debug(
            "Added buffer in %s with instance name %s", self.name, buffer_inst.name
        )

    # def sanity_check_cables(self):
    #     allWires = list(self.get_wires())
    #     for eachCables in self.get_cables():
    #         ww = eachCables.wires
    #         assert eachCables.is_scalar == (len(ww) == 1), \
    #             f"Wrong is_scalar attribute for {eachCables.name}"
    #         for eachWire in ww:
    #             assert eachWire.cable == eachCables, \
    #                 f"Wrong cable attribute on wire {eachWire} "
    #             allWires.remove(eachWire)
    #     assert allWires == [], "{len(allWires)} Wires are not in cables"

    # def sanity_check_ports(self):
    #     allPins = list(self.get_pins())
    #     for eachPort in self.get_ports():
    #         pp = eachPort.pins
    #         assert eachPort.is_scalar == (len(pp) == 1), \
    #             f"Wrong is_scalar attribute for {eachPort.name}"
    #         for eachPin in pp:
    #             assert eachPin.port == eachPort, \
    #                 f"Wrong cable attribute on wire {eachPin} "
    #             allPins.remove(eachPin)
    #     assert allPins == [], "{len(allPins)} Wires are not in cables"

    def clean_single_bit_assign(self, pattern="*ASSIGN*"):
        assign_instance = list(self.get_instances(pattern))
        for instance in assign_instance:
            in_pins = next(instance.get_ports("i")).pins
            out_pins = next(instance.get_ports("o")).pins
            if len(in_pins) == 1:
                in_net_name = instance.pins[in_pins[0]].wire.cable.name
                out_net_name = instance.pins[out_pins[0]].wire.cable.name
                is_in_port = instance.pins[in_pins[0]].wire.cable.is_port_cable
                is_out_port = instance.pins[out_pins[0]].wire.cable.is_port_cable
                if is_in_port and is_out_port:
                    logger.info(
                        f"Cant Flatten {instance.name} {in_net_name} {out_net_name}"
                    )
                elif not is_in_port and is_out_port:
                    for pin in list(instance.pins[in_pins[0]].wire.pins):
                        pin.wire.disconnect_pin(pin)
                        instance.pins[out_pins[0]].wire.connect_pin(pin)
                    self.remove_child(instance)
                    logger.info(
                        f"Merged nets {instance.name} {in_net_name} {out_net_name}"
                    )
                elif is_in_port and not is_out_port:
                    for pin in list(instance.pins[out_pins[0]].wire.pins):
                        pin.wire.disconnect_pin(pin)
                        instance.pins[in_pins[0]].wire.connect_pin(pin)
                    self.remove_child(instance)
                    logger.info(
                        f"Merged nets {instance.name} {in_net_name} {out_net_name}"
                    )
                elif not is_in_port and not is_out_port:
                    logger.info(
                        f"these nets be merged {instance.name} {in_net_name} {out_net_name}"
                    )
                elif (len(instance.pins[in_pins[0]].wire.pins) == 1) or (
                    len(instance.pins[out_pins[0]].wire.pins) == 1
                ):
                    logger.info("Removing undriven instance")
                    self.remove_child(instance)
