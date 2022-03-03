import unittest
import json
from unittest.case import expectedFailure
import spydrnet as sdn
from collections import OrderedDict
from spydrnet.util.hierarchical_reference import HRef
from spydrnet_physical.composers.html.composer import HTMLComposer


class TestHTMLComposer(unittest.TestCase):

    def setUp(self) -> None:
        self.composer = HTMLComposer()

    def _create_example_netlist(self) -> None:
        """ Create dummy hierarchy
        hier_top_instance
            ┣ inst_1
            ╏   ┣ inst_11
            ╏   ┗ inst_12
            ┗ inst_2
                ┣ inst_11
                ┗ inst_12

        """
        self.netlist = sdn.Netlist()
        library = self.netlist.create_library()
        top_module = library.create_definition(name="top")
        self.mod1 = library.create_definition()

        self.inst_1 = top_module.create_child(name="inst_1",
                                              reference=self.mod1)
        self.inst_2 = top_module.create_child(name="inst_2",
                                              reference=self.mod1)

        self.mod11 = library.create_definition()

        self.inst_11 = self.mod1.create_child(name="inst_11",
                                              reference=self.mod11)
        self.inst_12 = self.mod1.create_child(name="inst_12",
                                              reference=self.mod11)

        self.top = sdn.Instance()
        self.top.reference = top_module
        self.top.name = "hier_top_instance"
        self.netlist.top_instance = self.top

    def match_output(self, expectedOutput, Output):
        if isinstance(expectedOutput, str):
            expectedOutput = json.dumps(expectedOutput, sort_keys=True,
                                        separators=(',', ':'))
        if isinstance(Output, str):
            Output = json.dumps(Output, sort_keys=True,
                                separators=(',', ':'))
        assert expectedOutput == Output
        return True

    def test_write_json(self):
        ELKString = """{\n  "id": "1",\n  "hwMeta": { "name": "wire", "bodyText": "something"},\n  "children": []}""".strip()
        self.composer.ElkJSON = json.loads(ELKString)
        writtenStr = self.composer._write_json()
        assert ELKString == str(writtenStr), "JSON format is not compacted"

    def test_get_default_module_template(self):
        ELKJsonObj = {
            "id": "top/instance",
            "ports": [],
            "_children": [],
            "_edges": [],
            "hwMeta": {"bodyText": "instanceName", "cls": "Process", },
            "properties": {
                "org.eclipse.elk.layered.mergeEdges": 1,
                "org.eclipse.elk.portConstraints": "FIXED_SIDE"
            }
        }
        output = self.composer._get_default_module_template(
            "top/instance", "instanceName")
        self.assertTrue(self.match_output(ELKJsonObj, output),
                        "Wrong default value for module")

    def test_get_default_port_template(self):
        PortName = "ModulePort"
        port = sdn.Port(name=PortName, direction=sdn.Port.Direction.IN)
        ELKJsonObj = {
            "id": PortName,
            "direction": "INPUT",
            "hwMeta": {"name": PortName},
            "properties": {
                "index": 1,
                "side": "WEST"
            }
        }
        output = self.composer._get_default_port_template(port)
        self.assertIsInstance(output, OrderedDict)
        self.assertTrue(self.match_output(ELKJsonObj, output),
                        "Wrong default value for port")

        port.direction = sdn.Port.Direction.OUT
        ELKJsonObj["direction"] = "OUTPUT"
        ELKJsonObj["properties"]["side"] = "EAST"
        output = self.composer._get_default_port_template(port)
        self.assertIsInstance(output, OrderedDict)
        self.assertTrue(self.match_output(ELKJsonObj, output),
                        "Wrong default value for port")

    def test_get_default_net_template(self):
        cablename = "mycable"
        cable = sdn.Cable(name=cablename)
        ELKJsonObj = {
            "id": cablename,
            "hwMeta": {"name": cablename, "cssClass": "link-style0"},
            "sources": [],
            "targets": [],
        }
        output = self.composer._get_default_net_template(cable.name)
        self.assertIsInstance(output, OrderedDict)
        self.assertTrue(self.match_output(ELKJsonObj, output),
                        "Wrong default value for port")

    def test_create_top_frame(self):
        ELKJsonObj = {
            "id": "top_frame",
            "ports": [],
            "children": [],
            "edges": [],
            "hwMeta": {},
            "properties": {
                "org.eclipse.elk.layered.mergeEdges": 1,
                "org.eclipse.elk.portConstraints": "FIXED_SIDE"
            }
        }

        output = self.composer._create_top_frame()
        self.assertIsInstance(output, OrderedDict)
        self.assertTrue(self.match_output(ELKJsonObj, output),
                        "Wrong default value for port")

    def test_create_top_block(self):
        top_module_name = "top_module"
        self.composer.top_instance = top_module_name
        ELKJsonObj = {
            "id": top_module_name,
            "ports": [],
            "_children": [],
            "_edges": [],
            "hwMeta": {"bodyText": top_module_name,
                       "cls": "Process"},
            "properties": {
                "org.eclipse.elk.layered.mergeEdges": 1,
                "org.eclipse.elk.portConstraints": "FIXED_SIDE"
            }
        }
        output = self.composer._create_top_block(top_module_name)
        self.assertIsInstance(output, OrderedDict)
        self.assertTrue(self.match_output(ELKJsonObj, output),
                        "wrong top block format")

    def test_create_component_body(self):
        inport = "in_port"
        outport = "out_port"
        hinport = f"inst_1/inst_11/{inport}"
        houtport = f"inst_1/inst_11/{outport}"
        ELKJsonObj = {"ports": [
            {
                "id": hinport,
                "direction": "INPUT",
                "hwMeta": {"name": inport},
                "properties": {"index": 1, "side": "WEST"}},
            {
                "id": houtport,
                "direction": "OUTPUT",
                "hwMeta": {"name": outport},
                "properties": {"index": 1, "side": "EAST"}}
        ]}
        currNode = OrderedDict()
        currNode["ports"] = []
        self._create_example_netlist()
        self.mod11.create_port(name=outport,
                               direction=sdn.Port.Direction.OUT)
        self.mod11.create_port(name=inport,
                               direction=sdn.Port.Direction.IN)
        hInst = HRef.from_sequence([self.top, self.inst_1, self.inst_11])
        self.composer._create_component_body(hInst, currNode)
        print(json.dumps(currNode, indent=2))
        print(json.dumps(ELKJsonObj, indent=2))
        self.assertTrue(self.match_output(ELKJsonObj, currNode),
                        "Wrong default value for port")

    def test_add_edges_1(self):
        inport = "in_port"
        outport = "out_port"
        innet = "in_net"
        outnet = "out_net"
        self._create_example_netlist()
        p1 = self.mod1.create_port(name=outport,
                                   direction=sdn.Port.Direction.OUT).create_pin()
        p2 = self.mod1.create_port(name=inport,
                                   direction=sdn.Port.Direction.IN).create_pin()
        p11 = self.mod11.create_port(name=outport,
                                     direction=sdn.Port.Direction.OUT).create_pin()
        p12 = self.mod11.create_port(name=inport,
                                     direction=sdn.Port.Direction.IN).create_pin()

        n1 = self.mod1.create_cable(name=outnet).create_wire()
        n1.connect_pin(p1)
        n1.connect_pin(self.inst_11.pins[p11])

        n2 = self.mod1.create_cable(name=innet).create_wire()
        n2.connect_pin(p2)
        n2.connect_pin(self.inst_11.pins[p12])

        hInst = HRef.from_sequence([self.top, self.inst_1])

        ELKJsonObj = {
            "_edges": [
                {
                    "id": 1,
                    "hwMeta": {"name": f"inst_1/{outnet}", "cssClass": "link-style0"},
                    "sources": [["inst_1", f"inst_1/{outport}"]],
                    "targets": [["inst_1/inst_11", f"inst_1/inst_11/{outport}"]]
                }, {
                    "id": 2,
                    "hwMeta": {"name": f"inst_1/{innet}", "cssClass": "link-style0"},
                    "sources": [["inst_1", f"inst_1/{inport}"]],
                    "targets": [["inst_1/inst_11", f"inst_1/inst_11/{inport}"]]
                }]}
        currNode = OrderedDict()
        currNode["_edges"] = []
        self.composer._add_edges(hInst, currNode)
        print(json.dumps(currNode, indent=2))
        print(json.dumps(ELKJsonObj, indent=2))
        self.assertTrue(self.match_output(ELKJsonObj, currNode),
                        "Wrong default value for port")

    @expectedFailure
    def test_add_edges_2(self):
        inport = "in_port"
        outport = "out_port"
        innet = "in_net"
        outnet = "out_net"
        self._create_example_netlist()
        p1 = self.mod1.create_port(name=outport,
                                   direction=sdn.Port.Direction.OUT)
        p1.create_pins(4)
        p2 = self.mod1.create_port(name=inport,
                                   direction=sdn.Port.Direction.IN)
        p2.create_pins(4)
        p11 = self.mod11.create_port(name=outport,
                                     direction=sdn.Port.Direction.OUT)
        p11.create_pins(4)
        p12 = self.mod11.create_port(name=inport,
                                     direction=sdn.Port.Direction.IN)
        p12.create_pins(4)

        c2 = self.mod1.create_cable(name=outnet)
        c2.create_wires(4)
        c2.connect_port(p1)
        c2.connect_instance_port(self.inst_11, p11)

        c1 = self.mod1.create_cable(name=innet)
        c1.create_wires(4)
        c1.connect_port(p2)
        c1.connect_instance_port(self.inst_11, p12)

        hInst = HRef.from_sequence([self.top, self.inst_1])

        ELKJsonObj = {
            "_edges": [
                {
                    "id": 1,
                    "hwMeta": {"name": f"inst_1/{outnet}", "cssClass": "link-style1"},
                    "sources": [["inst_1", f"inst_1/{outport}"]],
                    "targets": [["inst_1/inst_11", f"inst_1/inst_11/{outport}"]]
                }, {
                    "id": 2,
                    "hwMeta": {"name": f"inst_1/{innet}", "cssClass": "link-style1"},
                    "sources": [["inst_1", f"inst_1/{inport}"]],
                    "targets": [["inst_1/inst_11", f"inst_1/inst_11/{inport}"]]
                }]}
        currNode = OrderedDict()
        currNode["_edges"] = []
        self.composer._add_edges(hInst, currNode)
        print(json.dumps(currNode, indent=2))
        print(json.dumps(ELKJsonObj, indent=2))
        self.assertTrue(self.match_output(ELKJsonObj, currNode),
                        "Wrong default value for port")
