import unittest
import spydrnet as sdn
from spydrnet_physical.util.get_names import get_names

class TestInstance(unittest.TestCase):

    def setUp(self):
        self.netlist = sdn.Netlist("test_netlist")
        self.library = self.netlist.create_library("test_lib")
    
    def test_check_all_scalar_connections(self):
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

        self.assertEqual(sm_inst.check_all_scalar_connections(sm_in1), True)
        self.assertEqual(sm_inst.check_all_scalar_connections(sm_in2), False)


    
    


