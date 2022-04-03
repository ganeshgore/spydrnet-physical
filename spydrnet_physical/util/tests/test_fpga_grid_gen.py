from random import randint, random
import tempfile
import unittest
import xml.etree.ElementTree as ET
import random
import spydrnet as sdn
from spydrnet_physical.ir.element import Element
from  spydrnet_physical.util import fpga_grid_gen, OpenFPGA_Arch, FPGAGridGen


class FpgaGridGen(unittest.TestCase):
    def setUp(self):
        self.design_name = "example_design"
        self.openfpga_arch = '''
        <openfpga_architecture>
        </openfpga_architecture>
        '''
        self.vpr_arch = '''
        <architecture>
            <tiles>
                <tile name="io_top" capacity="6" area="0"/>
                <tile name="io_right" capacity="6" area="0"/>
                <tile name="io_bottom" capacity="6" area="0"/>
                <tile name="io_left" capacity="6" area="0"/>
                <tile name="clb" width="1" height="1" area="0"/>
                <tile name="dsp" width="2" height="1" area="0"/>
                <tile name="ram9k" width="1" area="0"/>
            </tiles>

            <layout tileable="true" through_channel="true">
                <fixed_layout name="basicLayout" width="16" height="20">
                    <row type="io_top" starty="H-1" priority="100"/>
                    <row type="io_bottom" starty="0" priority="100"/>
                    <col type="io_left" startx="0" priority="100"/>
                    <col type="io_right" startx="W-1" priority="100"/>
                    <corners type="clb" priority="101"/>
                    <fill type="clb" priority="10"/>
                    <region type="dsp" startx="3" endx="W-3" starty="H/2" incry="H" priority="30"/>
                    <region type="ram9k" startx="3" endx="W-3" starty="5" incry="5" priority="20"/>
                </fixed_layout>
            </layout>
        </architecture>
        '''

        self.vpr_arch_et = ET.fromstring(self.vpr_arch)
        self.ofpga_et = ET.fromstring(self.openfpga_arch)
        self.fpga_arch = OpenFPGA_Arch(self.vpr_arch_et, self.ofpga_et, "basicLayout")
        self.fpga_grid_gen = FPGAGridGen(self.design_name, "./_fpga_grid_gen_arch.xml", "basicLayout", "./")
        self.layout_str = "basicLayout"
        self.element = Element()
        
    def test_init(self):
        tiles = {"io_top": (1, 1),   
                "io_right": (1, 1),
                "io_bottom": (1, 1),
                "io_left": (1, 1),
                "clb": (1, 1),
                "dsp":(2, 1),
                "ram9k":(1, 1),
                "EMPTY":(1,1)}
        self.assertDictEqual(self.fpga_arch.tiles, tiles)

    def test_get_blocks(self):
        _width = self.fpga_grid_gen.get_width()
        _height = self.fpga_grid_gen.get_height()
        _x, _y = random.randint(0, _width), random.randint(0, _height) 
        
        get_block_return = (0, _x , _y)
        self.assertTupleEqual(self.fpga_grid_gen.get_block(_x,_y), get_block_return)

    def test_add_fill(self):
        _width = self.fpga_grid_gen.get_width()
        _height = self.fpga_grid_gen.get_height()
        self.fpga_grid_gen.add_fill(self.element)
        for [x,y] in random.randint(0,_width), random.randint(0,_height):
            self.assertEqual(self.fpga_grid_gen.get_block(x,y) ,[x,y])

    def test_add_corner(self):
        self.arch_tree = ET.parse("./_fpga_grid_gen_arch.xml")
        self.root = self.arch_tree.getroot()
        self.layout = self.root.find(f".//fixed_layout[@name='{self.layout_str}']")
        # for element in sorted(self.layout, key=lambda x: int(x.attrib["priority"])):
        #     if element.tag.lower()=='io_top':
        #         self.ele_type = element.attrib["type"].lower()
        # # self.ele_type = self.ele.attrib['type']
        # # self.fpga_grid_gen.layout
        # self.fpga_grid_gen.add_corners(self.ele_type)
        # self.assertEqual(self.fpga_grid_gen.get_block(0,0), (1,0,0))

    # workinprogress


    def test_add_col(self):
        assert(True) 

    def test_add_region(self):
        assert(True) 

    def test_enumerate_grid(self):
        list2=[
            []
        ]
        assert(True)
        # self.assertListEqual(self.fpga_grid_gen.enumerate_grid(), list2)