''' Tst cases fro get_names method '''
import unittest
import tempfile
import xml.etree.ElementTree as ET
from spydrnet import ir
from spydrnet_physical.util import get_names, get_attr, OpenFPGA_Arch


class TestOpenFPGAArch(unittest.TestCase):
    ''' Test case class '''

    def setUp(self):
        ''' Basic element setup '''
        self.openfpga_arch = '''
        <openfpga_architecture>
        </openfpga_architecture>
        '''
        self.vpr_arch = '''
        <architecture>
            <complexblocklist>
                 <pb_type name="io"/>
                 <pb_type name="clb"/>
                 <pb_type name="ram"/>
            </complexblocklist>
            <layout tileable="true">
                <fixed_layout name="base" width="6" height="6"/>
                <fixed_layout name="plus" width="12" height="12"/>
                <fixed_layout name="ultimate" width="64" height="64"/>
            </layout>
        </architecture>
        '''
        self.vpr_arch_et = ET.fromstring(self.vpr_arch)
        self.ofpga_et = ET.fromstring(self.openfpga_arch)
        self.fpga_arch = OpenFPGA_Arch(self.vpr_arch_et, self.ofpga_et, "base")

    def test_init(self):
        pb_types = {"io": (1, 1),
                    "clb": (1, 1),
                    "ram": (1, 1)}
        self.assertDictEqual(self.fpga_arch.pb_types, pb_types)

    def test_get_layouts(self):
        layouts = {"base": (6, 6), "plus": (12, 12), "ultimate": (64, 64)}
        self.assertDictEqual(self.fpga_arch.get_layouts(), layouts)

    def test_set_layout(self):
        self.fpga_arch.set_layout("plus")
        self.assertIsInstance(self.fpga_arch.layout, ET.Element)
        self.assertEqual(self.fpga_arch.layout.attrib["name"], "plus")

    def test_is_homogeneous(self):
        ''' TODO: Write tet to check if layout contains anything other than 
        `corner`, `periphery`, `fill` tags 
        '''
        pass
