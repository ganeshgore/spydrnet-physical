
import logging

import spydrnet as sdn
from spydrnet.ir import Definition as DefinitionBase
from itertools import combinations

logger = logging.getLogger('spydrnet_logs')



class Definition(DefinitionBase):
    """
    Extending the definitions representation
    """

    def _disconnect_port(self, port):
        '''
        This method disconnects the definition port from its cable
        This makes the port dangling, this method is used before
        removing the port
        '''
        assert port in self._ports, "Port does not belong to this definition"
        for pin in port.pins:
            if pin.wire:
                pin.wire.disconnect_pin(pin)
            del pin

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

    def create_feedthroughs_ports(self, cable, suffix="ft"):
        '''
        Given the cable object it creates a feedthrough ports on this definition

        - The new ports names as {cable_name}_{suffix}_in and {cable_name}_{suffix}_out - Direct assignment is created beetween newly added two ports

        args:
            cable (Port): The cable for which feedthrough needs to be created
            suffix (str): Sufffix used for the port naming

        Returns:
            tuple: Feedthrough port (inport and outport)
        '''
        inport_name = f"{cable.name}_{suffix}_in"
        outport_name = f"{cable.name}_{suffix}_out"
        inport, outport = (
            self.create_port(inport_name,
                             pins=cable.size,
                             is_scalar=cable.is_scalar,
                             lower_index=cable.lower_index,
                             direction=sdn.IN),
            self.create_port(outport_name,
                             pins=cable.size,
                             is_scalar=cable.is_scalar,
                             lower_index=cable.lower_index,
                             direction=sdn.OUT))

        int_cable = self.create_cable(inport_name, wires=cable.size)
        out_cable = self.create_cable(outport_name, wires=cable.size)

        assign_library = self._get_assignment_library()
        definition = self._get_assignment_definition(
            assign_library, cable.size)
        instance = self.create_child(
            f"{inport_name}_{outport_name}_ft",
            reference=definition)

        int_cable.connect_port(inport)
        int_cable.connect_instance_port(
            instance, next(definition.get_ports("i")))
        out_cable.connect_port(outport)
        out_cable.connect_instance_port(
            instance, next(definition.get_ports("o")))
        return (inport, outport)

    def create_feedthrough(self, instances_list, cable):
        """
        Creates a feedthrough for a single cable passing through
        list of instances

        The driver cable name is unchanged and newly created feedthrough cable
        name {cable_name}_ft_{indx}

        parameters
        ----------

        instances_list (list[instance]): List of instances to create
                                        feedthrough from
        cable (Cable): cable fro which feedthrough needs to be creared

        Returns:
        --------
            list(Cable): List of newly created cables in order
        """
        if isinstance(instances_list, sdn.Instance):
            instances_list = (instances_list,)
        assert len(instances_list) > 0, \
            "Missing instances to create feedthroughs"
        assert isinstance(cable, sdn.Cable), \
            "Cable object required"
        assert cable.definition == self, \
            "Cable {cable.name} does not belog to thos definition"

        cable_list = []
        for indx, instance in enumerate(instances_list):
            inport, outport = instance.reference.create_feedthroughs_ports(
                cable)
            cable_name = cable.name
            cable.name = f"{cable.name}_ft_in_{indx}"
            new_cable = self.create_cable(cable_name)
            new_cable.create_wires(cable.size)
            new_cable.connect_instance_port(instance, inport)
            for each_w in cable.wires:
                for pin in each_w.pins:
                    if pin.port.direction == sdn.OUT:
                        each_w.disconnect_pin(pin)
                        new_cable.wires[pin.inner_pin.index()].connect_pin(pin)
            cable.connect_instance_port(instance, outport)
            cable_list.append(new_cable)
        return cable_list

    def create_feedthrough_multiple(self, instances_list):
        """
        This creates feedthough from list of instances on multiple locations
        Expects the list of tuples in following format

        parameters
        ----------

        instances_list: [(Cable, (inst1, inst1, . . . .instn), ...
                        (Cable, (inst1, inst1, . . . .instn))]
        """
        assert len(instances_list) > 0, \
            "Missing instances list to create feedthroughs"

        for cable, inst_tuple in instances_list:
            assert isinstance(cable, sdn.Cable), \
                "Cable object required"
            assert cable.definition == self, \
                "Cable {cable.name} does not belog to thos definition"
            for indx, instance in enumerate(inst_tuple):
                assert isinstance(instance, sdn.Instance), \
                    "Found {type(instance) in the instances list}"
                assert instance.reference == instances_list[0][1][indx].reference, \
                    f"Instances order does not match"

        new_cables = []
        port_map = []
        for indx2, instance in enumerate(instances_list[0][1]):
            inport, outport = instance.reference.create_feedthroughs_ports(
                instances_list[0][0], suffix=f"ft_{indx2}")
            port_map.append((inport, outport))

        for indx2, instances_list in enumerate(instances_list):
            for indx, inst in enumerate(instances_list[1][::-1]):
                cable = instances_list[0]
                logger.info(f"Iterating {cable.name} for inst {inst.name}")

                new_cable = self.create_cable(f"{cable.name}_ft_{indx}")
                new_cable.create_wires(cable.size)

                logger.info(f"Created new cable {cable.name} {new_cable.name}")
                new_cables.append(new_cable)
                new_cable.connect_instance_port(inst, port_map[indx][1])
                for each_w in cable.wires:
                    for pin in each_w.pins:
                        if pin.port.direction == sdn.IN:
                            each_w.disconnect_pin(pin)
                            new_cable.wires[pin.inner_pin.index()].connect_pin(
                                pin)
                cable.connect_instance_port(inst, port_map[indx][0])
        return new_cables, port_map

    # def merge_multiple_instance(self, instances_list_tuple, new_definition_name=None, pin_map=None):
    #     """
    #     This method can merge multiple group of instances having same reference.
    #     First pair of the instances_list_tuple is used to create new definition
    #     and this def is reuse while grouping remaining group of instances
    #     instances_list_tuple = [(inst_1, inst_2, ...., inst_n), <instance_name>]
    #     new_definition_name = Name for the new definition
    #     pin_map             = Function of dictionary to rename pins
    #     """
    #     mainDef = None
    #     instance_list = []
    #     for instances_list, instance_name in instances_list_tuple:
    #         newDef, newInst, _ = self.merge_instance(instances_list,
    #                                                  new_definition_name=f"{new_definition_name}_{instance_name}",
    #                                                  new_instance_name=instance_name,
    #                                                  pin_map=pin_map)
    #         instance_list.append(newInst)
    #         if not mainDef:
    #             mainDef = newDef
    #             mainDef.name = new_definition_name
    #         else:
    #             newInst.reference = mainDef
    #             self.library.remove_definition(newDef)
    #     return mainDef, instance_list

    # def merge_instance(self, instances_list, new_definition_name=None, new_instance_name=None, pin_map=None):
    #     """
    #     instances_list      : List of instances to be merged
    #     new_definition_name : Name of the new definition created
    #     new_instance_name   : Name of the new instance created
    #     pin_map : function or a dictionary mapping pin of each module
    #               function call arguments:
    #               get_pin_name(<definition_name:<str>, <pin_name:<str>,
    #                             <instance_name:<str>)
    #     """
    #     RenameMap = {}  # Stores the final rename map

    #     # ====== Input Sanity checks
    #     for eachModule in instances_list:
    #         assert isinstance(
    #             eachModule, Instance), "Modulelist contains none non-intance object"

    #     if pin_map:
    #         if isinstance(pin_map, dict):
    #             pin_map_copy = pin_map
    #             def pin_map(x, y, _): return pin_map_copy.get(x, {}).get(y, {})
    #         if not callable(pin_map):
    #             print(
    #                 "pin_map argument should be dictionary or function, received {type(pin_map)}")

    #     # ====== Create a new definition
    #     if not new_definition_name:
    #         new_def_name = "_".join(
    #             [each.reference.name for each in instances_list]) + "_merged"
    #         print(f"Inferred definition name {new_def_name} ")
    #     else:
    #         new_def_name = new_definition_name
    #     newMod = self.library.create_definition(name=new_def_name)

    #     # ===== Create instance of the definition
    #     if not new_instance_name:
    #         new_instance_name = f"{new_def_name}_1"
    #     MergedModule = self.create_child(name=new_instance_name,
    #                                      reference=newMod)

    #     # ===== Interate over each module and create new module
    #     for index, eachM in enumerate(instances_list):

    #         RenameMap[eachM.reference.name] = {}
    #         RenameMap[eachM.reference.name][index] = {}
    #         currMap = RenameMap[eachM.reference.name][index]
    #         IntInst = newMod.create_child(name=eachM.name,
    #                                       reference=eachM.reference)
    #         # Iterate over each port of current instance
    #         for p in eachM.get_ports():
    #             pClone = p.clone()  # It copied all pins, wires and cables

    #             for eachSuffix in [""]+[f"_{i}" for i in range(10)]:
    #                 newName = pClone.name + eachSuffix
    #                 if not len(list(newMod.get_ports(newName))):
    #                     break
    #             newCable = newMod.create_cable(
    #                 name=newName,
    #                 is_downto=pClone.is_downto,
    #                 is_scalar=pClone.is_scalar,
    #                 lower_index=pClone.lower_index,
    #             )

    #             # Create connection inside new definition
    #             for eachPClone, eachP in zip(pClone.pins, p.pins):
    #                 w = newCable.create_wire()
    #                 w.connect_pin(eachPClone)
    #                 w.connect_pin(IntInst.pins[eachP])
    #             pClone.change_name(newName)
    #             newMod.add_port(pClone)

    #             currMap[p.name] = newName

    #             for eachPin in p.pins:
    #                 instOutPin = eachM.pins[eachPin]
    #                 conWire = instOutPin.wire
    #                 instPin = MergedModule.pins[pClone.pins[eachPin.index()]]
    #                 conWire.connect_pin(instPin)
    #                 instOutPin.wire.disconnect_pin(instOutPin)
    #                 newCable.wires[eachPin.index()].connect_pin(instOutPin)

    #         self.remove_child(eachM)
    #     return newMod, MergedModule, RenameMap

    def OptPins(self, pins=lambda x: True, dry_run=False, merge=True, absorb=True):
        """
        This method optimizes the definitions pins bu inspecting all the
        instances of the definition

        parameters
        ----------

        dry_run: Just performs the dryrun and list the pins which can be merged or absorbed
        pins: only consider specific pins, provide filter function
        absorb: if two pins are only connected to each other they will be absorbed and internal connection will be made
        merge: if two pins are connected to each other and few other instances, one of the pin will be absorbed and other will exist
        """
        duplicatePins = []  # Set of all pins which can be merged or absorbed
        absorbPins = []  # Subset of duplicate pins
        defPort = list([x for x in self.get_ports() if pins(x.name)])

        # Iterate over all the ports pairs of the definition
        for fromPort, toPort in combinations(defPort, 2):
            if len(fromPort.pins) == len(toPort.pins):
                # Compare only when port has same width
                sameNet = True
                singleWire = True
                for eachPin1, eachPin2 in zip(fromPort.pins, toPort.pins):
                    for eachInst in self.references:
                        eachPin1 = eachInst.pins[eachPin1]
                        eachPin2 = eachInst.pins[eachPin2]
                        if not eachPin1.wire == eachPin2.wire:
                            sameNet = False
                            break
                        elif singleWire:
                            singleWire = set(eachPin1.wire.pins) == set(
                                (eachPin1, eachPin2))

                if sameNet:
                    # Check if frompin exist in the previous pairs
                    already_paired = next(
                        (dupliPins for dupliPins in duplicatePins if fromPort in dupliPins), None)
                    if already_paired:
                        if not toPort in already_paired:
                            already_paired.append(toPort)
                    else:
                        portPair = [fromPort, toPort]
                        duplicatePins.append(portPair)
                    if singleWire:
                        absorbPins.append(portPair)

        if not dry_run:
            for ports in duplicatePins[::-1]:

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
                    logger.debug(
                        f"Merged Ports {ports[0].name}<-{eachPort.name}")
                if ports in absorbPins:
                    self.remove_port(ports[0])
                    logger.debug(f"Absorbed port {ports[0].name}")

        return duplicatePins if merge else absorbPins if absorb else None

    # TODO : Need to consider floating paraters
    def OptWires(self, no_load=True,  no_driver=False, floating=True):
        '''
        List the wires which can be optimised based on different constraints

        parameters
        ----------

        no_load: (bool) (Default: True) Wires without load pin
        no_driver: (bool) (Default: False) Wires without drivers pin
        floating: (bool) (Default: True) Wires without any connection to pin
        '''
        for cable in self.get_cables():
            for wire in cable.wires:
                if (len(wire.pins) < 2):
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
        '''
        Returns assignment library from the netlist of this definition.
        If the assignment library is missing it will create new and return
        '''
        assert self.library, "Library is not defined for the definition"
        assert self.library.netlist, \
            "netlist is not defined for the library definition"
        netlist = self.library.netlist
        assign_library = next(netlist.get_libraries(
            "SDN_VERILOG_ASSIGNMENT"), None)
        if assign_library is None:
            logger.info("Missing SDN_VERILOG_ASSIGNMENT libarary Creating new")
            assign_library = netlist.create_library(
                name="SDN_VERILOG_ASSIGNMENT")
        return assign_library

    def _get_assignment_definition(self, assign_library, size):
        '''
        Returns assignment definition for the give size

        parameters
        ----------

        assign_library = ``SDN_VERILOG_ASSIGNMENT`` library
        size = (int) Size of the assignment block
        '''
        assign_def_name = f"SDN_VERILOG_ASSIGNMENT_{size}"
        definition = next(
            assign_library.get_definitions(assign_def_name), None)
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
        '''
        Duplicates existing port in the definition
        Uses assign block beetween to short two cables
        If post in output port ``assign new_port = initial_port``
        else ``assign initial_port = new_port``

        parameters
        ----------

        port: (Port) Port of this definition
        port_name: (str) Options New port name (default {port_name}_dup)
        '''
        assert isinstance(port, sdn.Port), \
            f"Required Port but found {type(port)}"

        assert self.library, "Library is not defined for the definition"
        assert self.library.netlist, "netlist is not defined for the library definition"

        new_port = port.clone()
        new_port.name = port_name if port_name else f"{port.name}_dup"
        port_cable = port.pins[0].wire.cable
        new_cable = port_cable.clone()
        new_cable.name = new_port.name
        new_cable.connect_port(new_port)

        assign_library = self._get_assignment_library()
        definition = self._get_assignment_definition(
            assign_library, new_cable.size)

        instance = self.create_child(f"SDN_ASSIGNMENT_{port.name}_{new_port.name}",
                                     reference=definition)
        if port.is_output:
            port_cable.connect_instance_port(
                instance, next(definition.get_ports("i")))
            new_cable.connect_instance_port(
                instance, next(definition.get_ports("o")))
        else:
            new_cable.connect_instance_port(
                instance, next(definition.get_ports("i")))
            port_cable.connect_instance_port(
                instance, next(definition.get_ports("o")))
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
            assert isinstance(c, sdn.Cable), \
                f"combine_cables can combine only cable found {type(c)}"
            assert self == c.definition, \
                f"all ports to combine should belong to same definition"
            assert cables.count(c) == 1, \
                f"Cable defined multiple times {c.name}"

        newCable = self.create_cable(new_cable_name, is_scalar=False)
        for c in cables[::-1]:
            for wire in c.wires[::-1]:
                c.remove_wire(wire)
                newCable.add_wire(wire)
            self.remove_cable(c)
        return newCable

    # def combine_ports(self, newPortName, ports):
    #     """ This can combine multiple input or output ports togther
    #         to create a bus structure.
    #     """
    #     direction = ports[0].direction
    #     for p in ports[1:]:
    #         assert isinstance(p, Port), \
    #             f"combine_ports can combine Ports found {type(p)}"
    #         assert direction == p.direction, \
    #             f"combine_ports combines only input or output ports, \
    #             found {type(p.direction)}"
    #         assert self == p.definition, \
    #             f"all ports to combine should belong to same definition"

    #     newPort = self.create_port(newPortName, direction=direction)
    #     newCable = self.create_cable(newPortName, is_scalar=newPort.is_scalar)
    #     for p in ports:
    #         newPin = newPort.create_pin()
    #         pp = p.pins[0]
    #         ppWire = pp.wire
    #         # Switch Instances connection
    #         for instance in self.references:
    #             if instance.pins[pp].is_connected:
    #                 instance.pins[pp].wire.connect_pin(instance.pins[newPin])
    #         if ppWire:
    #             # Switch Internal Wire
    #             ppWire.connect_pin(newPin)
    #             self.remove_cable(ppWire.cable)
    #             ppWire.cable.remove_wire(ppWire)
    #             newCable.add_wire(ppWire)
    #         logger.debug(f"Removing port {p.name}")
    #         self.remove_port(p)
    #     logger.debug(f"Combined with {newPort.name} " +
    #                  f"created cable {newCable.name}")
    #     return newPort, newCable

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
