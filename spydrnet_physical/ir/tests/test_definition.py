import unittest
from unittest.case import expectedFailure

import spydrnet as sdn
from spydrnet_physical.util.get_names import get_names


class TestDefinition(unittest.TestCase):
    def setUp(self):
        self.netlist = sdn.Netlist("test_netlist")
        self.library = self.netlist.create_library("test_lib")
        self.definition = self.library.create_definition()

    def test_create_feedthroughs_ports(self):
        ''' Test feedthrough port creation '''
        cable = sdn.Cable("cable1")
        cable.create_wires(4)

        port1, port2 = self.definition.create_feedthroughs_ports(cable, "feed")
        self.assertIsInstance(port1, sdn.Port)
        self.assertIsInstance(port2, sdn.Port)
        self.assertSetEqual(set(get_names(self.definition.get_ports())),
                            {"cable1_feed_in", "cable1_feed_out"})
        self.assertSetEqual(set(get_names(self.definition.get_cables())),
                            {'cable1_feed_in', 'cable1_feed_out'})

    def test_create_feedthroughs_ports_2(self):
        ''' Test feedthrough port creation with lambda naming '''
        cable = sdn.Cable("cable1")
        cable.create_wires(4)
        def get_port_name(x): return "inport" if x is sdn.IN else "outport"
        port1, port2 = self.definition.create_feedthroughs_ports(
            cable,
            get_port_names=get_port_name)
        self.assertIsInstance(port1, sdn.Port)
        self.assertIsInstance(port2, sdn.Port)
        self.assertSetEqual(set(get_names(self.definition.get_ports())),
                            {"inport", "outport"})

    def test_create_feedthrough(self):
        ''' This checks bus feedthrough from single instance '''

        module1 = self.library.create_definition("module1")
        module2 = self.library.create_definition("module2")
        driver_port = module1.create_port("driver", direction=sdn.OUT, pins=4)
        load_port = module1.create_port("load", direction=sdn.IN, pins=4)

        # Create instances
        inst0 = self.definition.create_child("inst0", reference=module1)
        inst1 = self.definition.create_child("inst1", reference=module1)
        ft_inst = self.definition.create_child("ft_inst", reference=module2)

        # Create cable
        cable = self.definition.create_cable("cable", wires=4)
        cable.connect_instance_port(inst0, driver_port)
        cable.connect_instance_port(inst1, load_port)

        # Create Feedthrough
        new_cables = self.definition.create_feedthrough(ft_inst, cable)

        # Check correctness of connections
        for new_cable in new_cables:
            self.assertTrue(isinstance(new_cable, sdn.Cable),
                            "Return value should be cable")
        new_cables = new_cables[0]
        self.assertEqual(new_cables.size, 4,
                         "New cable should have same dimensions")
        self.assertSetEqual(set(map(lambda p: p.name, module2.ports)),
                            {"cable_ft_out", "cable_ft_in"})
        self.assertSetEqual(set(map(lambda p: p.name, self.definition.get_cables())),
                            {"cable", "cable_ft_in_0"})
        self.assertSetEqual(set(('cable_ft_in_0', 'cable')),
                            set(get_names(ft_inst.get_cables(selection="OUTSIDE"))),
                            "Checks if both the cable are connected to feedthoguh instance")
        self.assertSetEqual(set(('cable',)),
                            set(get_names(inst0.get_cables(selection="OUTSIDE"))),
                            "Checks if original wire name is still same ")
        self.assertSetEqual(set(('cable_ft_in_0',)),
                            set(get_names(inst1.get_cables(selection="OUTSIDE"))),
                            "Checks if feethrough wire name is as expected ")

    def test_combine_ports(self):
        ''' Creates 3 port on the given definition and combines them '''
        port1 = self.definition.create_port(pins=1)
        port2 = self.definition.create_port(pins=1)
        port3 = self.definition.create_port(pins=1)

        cable1 = self.definition.create_cable(wires=1)
        cable1.connect_port(port1)
        wire1 = cable1.wires[0]

        cable2 = self.definition.create_cable(wires=1)
        cable2.connect_port(port2)
        wire2 = cable2.wires[0]

        cable3 = self.definition.create_cable(wires=1)
        cable3.connect_port(port3)
        wire3 = cable3.wires[0]

        new_port, new_cable = self.definition.combine_ports(
            "merged_port", [port1, port2, port3])

        self.assertIsInstance(new_port, sdn.Port)
        self.assertEqual(new_port.size, 3)
        self.assertIsInstance(new_cable, sdn.Cable)
        self.assertEqual(new_cable.size, 3)
        self.assertEqual(len(self.definition.ports), 1)
        self.assertEqual(new_port.pins[0].wire, wire1)
        self.assertEqual(new_port.pins[1].wire, wire2)
        self.assertEqual(new_port.pins[2].wire, wire3)

    def test_merge_instance(self):
        def2 = self.library.create_definition("def2")
        def3 = self.library.create_definition("def3")
        inst2 = self.definition.create_child("inst2", reference=def2)
        inst3 = self.definition.create_child("inst3", reference=def3)
        new_m, inst, pin_map = self.definition.merge_instance([inst2, inst3])

        self.assertTrue(new_m.name, "def2_def3_merged")
        self.assertTrue(inst.name, "def2_def3_merged_1")
        self.assertTrue(inst.reference, new_m)
        self.assertEqual(set(get_names(self.definition.get_instances())),
                         {"def2_def3_merged_1", })
        self.assertEqual(set(get_names(new_m.get_instances())),
                         {"inst2", "inst3"})

    def test_flatten_instance(self):
        submodule = self.library.create_definition("submodule")
        sm_in1 = submodule.create_port("sm_in1", direction=sdn.IN, pins=1)
        sm_in2 = submodule.create_port("sm_in2", direction=sdn.IN, pins=4)
        sm_out1 = submodule.create_port("sm_out1", direction=sdn.OUT,  pins=1)
        sm_out2 = submodule.create_port("sm_out2", direction=sdn.OUT,  pins=4)

        module = self.library.create_definition("module")
        in1 = module.create_port("in1", direction=sdn.IN, pins=1)
        in2 = module.create_port("in2", direction=sdn.IN, pins=4)
        out1 = module.create_port("out1", direction=sdn.OUT,  pins=1)
        out2 = module.create_port("out2", direction=sdn.OUT,  pins=4)
        sm_inst = module.create_child("submodule_inst", reference=submodule)

        in1_c = module.create_cable("in1", wires=1)
        in1_c.connect_instance_port(sm_inst, sm_in1)
        in2_c = module.create_cable("in2", wires=4)
        in2_c.connect_instance_port(sm_inst, sm_in2)
        out1_c = module.create_cable("out1", wires=1)
        out1_c.connect_instance_port(sm_inst, sm_out1)
        out2_c = module.create_cable("out2", wires=4)
        out2_c.connect_instance_port(sm_inst, sm_out2)

        inst1 = self.definition.create_child("inst1", reference=module)
        win1 = self.definition.create_cable("win1", wires=1)
        win1.connect_instance_port(inst1, in1)
        win2 = self.definition.create_cable("win2", wires=4)
        win2.connect_instance_port(inst1, in2)
        wout1 = self.definition.create_cable("wout1", wires=1)
        wout1.connect_instance_port(inst1, out1)
        wout2 = self.definition.create_cable("wout2", wires=4)
        wout2.connect_instance_port(inst1, out2)

        self.definition.flatten_instance(inst1)
        self.assertEqual(len(self.definition.children), 1)
        self.assertEqual(self.definition.children[0].name,
                         "inst1_submodule_inst")

    @expectedFailure
    def test_get_connectivity_network():
        assert 1 == 2

    
    def test_merge_multiple_instance(self):
        def2 = self.library.create_definition("def2")
        def3 = self.library.create_definition("def3")
        inst2 = self.definition.create_child("inst2", reference=def2)
        inst3 = self.definition.create_child("inst3", reference=def3)
        inst4 = self.definition.create_child("inst4", reference=def2)
        inst5 = self.definition.create_child("inst5", reference=def3)

        instance_list_tuple = [((inst2, inst3),'merged_inst_2_3'), ((inst4, inst5), "merged_inst_4_5")]

        new_def, inst_list = self.definition.merge_multiple_instance(instance_list_tuple, new_definition_name = 'new_merged_inst')

        merged_inst1 = inst_list[0]
        merged_inst2 = inst_list[1]

        self.assertEqual(new_def.name, 'new_merged_inst')
        self.assertEqual(merged_inst1.name, 'merged_inst_2_3')
        self.assertEqual(merged_inst2.name, 'merged_inst_4_5')


    def test_combine_cables(self):
        ''' Creates 3 port on the given definition and combines them '''
        port1 = self.definition.create_port(pins=1)
        port2 = self.definition.create_port(pins=1)
        port3 = self.definition.create_port(pins=1)

        cable1 = self.definition.create_cable(wires=1)
        cable1.connect_port(port1)
        wire1 = cable1.wires[0]

        cable2 = self.definition.create_cable(wires=1)
        cable2.connect_port(port2)
        wire2 = cable2.wires[0]

        cable3 = self.definition.create_cable(wires=1)
        cable3.connect_port(port3)
        wire3 = cable3.wires[0]

        new_cable = self.definition.combine_cables(
            "merged_cables", [cable1, cable2, cable3])

        self.assertIsInstance(new_cable, sdn.Cable)
        self.assertEqual(new_cable.size, 3)
        self.assertEqual(len(self.definition.ports), 3)

    def test_make_unique_instance(self):

        def1 = self.library.create_definition("def1")
        inst = self.definition.create_child("inst", reference= def1)

        new_def = self.definition.make_instance_unique(inst, "inst_new")
        
        self.assertEqual(new_def.name, "inst_new")


    def test_OptPins(self):
        top_def = self.library.create_definition("top_def")

        #defing the ios and cables for the top module
        top_in0_port = top_def.create_port(name="in0",direction=sdn.IN)
        top_in1_port = top_def.create_port(name="in1",direction=sdn.IN)
        top_out0_port = top_def.create_port(name="out0",direction=sdn.OUT)

        top_in0_pin = top_in0_port.create_pin()
        top_in1_pin = top_in1_port.create_pin()
        top_out0_pin = top_out0_port.create_pin()

        cable_io0 = top_def.create_cable(name="in0",is_scalar=True,wires=1)
        cable_io1 = top_def.create_cable(name = "in1", is_scalar=True, wires = 1)
        cable_out = top_def.create_cable(name = "out0", is_scalar=True, wires = 1)
        cable_wire = top_def.create_cable(name = "wire0", is_scalar=True, wires = 1)

        cable_io0.connect_port(top_in0_port,reverse=False)
        cable_io1.connect_port(top_in1_port,reverse=False)
        cable_out.connect_port(top_out0_port,reverse=False)

        #defing module 1
        def1 = self.library.create_definition("Module1")
        #defining the ports and pins
        def1_in0 = def1.create_port("in0", direction=sdn.IN)
        def1_in1 = def1.create_port("in1", direction=sdn.IN)
        def1_out = def1.create_port("out0", direction=sdn.OUT)

        mod1_in0_pin = def1_in0.create_pin()
        mod1_in1_pin = def1_in1.create_pin()
        mod1_out0_pin = def1_out.create_pin()

        cable_mod1in0 = def1.create_cable(name="in0",is_scalar=True,wires=1)
        cable_mod1in1 = def1.create_cable(name = "in1", is_scalar=True, wires = 1)
        cable_mod1out = def1.create_cable(name = "out", is_scalar=True, wires = 1)

        #creating the child instances
        inst1 = top_def.create_child("inst1", reference= def1)
        for ports in inst1.reference.get_ports():
            if ports.name == 'in0':
                inst_pin = inst1.pins[ports.pins[0]]
                next(top_def.get_cables("in0")).wires[0].connect_pin(inst_pin)
            elif ports.name == 'in1': 
                inst_pin = inst1.pins[ports.pins[0]]   
                next(top_def.get_cables("in1")).wires[0].connect_pin(inst_pin)
            else:
                inst_pin = inst1.pins[ports.pins[0]]
                next(top_def.get_cables("wire0")).wires[0].connect_pin(inst_pin)

        inst2 = top_def.create_child("inst2", reference= def1)
        for ports in inst2.reference.get_ports():
            if ports.name == 'in0':
                inst_pin = inst2.pins[ports.pins[0]]
                next(top_def.get_cables("wire0")).wires[0].connect_pin(inst_pin)
            elif ports.name == 'in1': 
                inst_pin = inst2.pins[ports.pins[0]]   
                next(top_def.get_cables("in0")).wires[0].connect_pin(inst_pin)
            else:
                inst_pin = inst2.pins[ports.pins[0]]
                next(top_def.get_cables("out0")).wires[0].connect_pin(inst_pin)


        new_m, inst, pin_map = top_def.merge_instance([inst1, inst2])
        port_list = [print(i.name) for i in new_m.ports]
        self.assertEqual(len(port_list), 6)
        #with merge = True
        new_m.OptPins()
        port_list = [print(i.name) for i in new_m.ports]
        self.assertEqual(len(port_list), 3)   


    def test_split_port(self):
        port = self.definition.create_port(name="in0", is_downto=True, is_scalar = False, lower_index = 0, direction=sdn.IN, pins=4)

        cable = self.definition.create_cable(name="in0",is_downto=True, is_scalar = False, lower_index = 0, wires=4)

        cable.connect_port(port)

        port_list = [print(i.name) for i in self.definition.ports]        

        self.assertEqual(len(port_list), 1)

        self.definition.split_port(port)

        port_list = [print(i.name) for i in self.definition.ports]        

        self.assertEqual(len(port_list), 4)


    def test_duplicate_port(self):
        port = self.definition.create_port( 
        name="in0", is_downto=True, is_scalar = False, lower_index = 0, direction=sdn.IN, pins=4)

        cable = self.definition.create_cable(name="in0",is_downto=True, is_scalar = False, lower_index = 0, wires=4)

        cable.connect_port(port)

        port_list = [print(i.name) for i in self.definition.ports]        

        self.assertEqual(len(port_list), 1)

        self.definition.duplicate_port(port)

        port_list = [print(i.name) for i in self.definition.ports]        

        self.assertEqual(len(port_list), 2)


    def test_create_unconn_wires(self):
        port = self.definition.create_port( 
        name="in0", is_downto=True, is_scalar = False, lower_index = 0, direction=sdn.IN, pins=1)

        cable_list = [print(i.name) for i in self.definition.cables]        

        self.assertEqual(len(cable_list), 0)

        self.definition.create_unconn_wires()

        cable_list = [print(i.name) for i in self.definition.cables]        

        self.assertEqual(len(cable_list), 1)

    



