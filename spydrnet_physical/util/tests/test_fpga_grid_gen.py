from random import randint, random
import tempfile
import unittest
import xml.etree.ElementTree as ET
import random
import spydrnet as sdn
from spydrnet_physical.ir.element import Element
from spydrnet_physical.util import FPGAGridGen, OpenFPGA_Arch, FPGAGridGen


class TestFpgaGridGen(unittest.TestCase):
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
        self.fpga_arch = OpenFPGA_Arch(
            self.vpr_arch_et, self.ofpga_et, "basicLayout")
        self.vprArchTree = ET.ElementTree(
            ET.fromstring(self.vpr_arch)).getroot()
        # self.fpga_grid_gen = FPGAGridGen(
        #     self.design_name, "./_fpga_grid_gen_arch.xml", "basicLayout", "./")
        self.layout_str = "basicLayout"
        self.element = Element()

    def test_init(self):
        '''
        Check self.fpga_arch is instance of OpenFPGA_Arch
        Check self.width, self.height of the object
        Check self.grid has a correct width and height
        '''

        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'basicLayout', "")

        self.assertIsInstance(grid_gen.fpga_arch, OpenFPGA_Arch)
        self.assertIs(grid_gen.width, 16)
        self.assertIs(grid_gen.height, 20)
        self.assertIs(len(grid_gen.grid), 20)
        self.assertIs(len(grid_gen.grid[0]), 16)

        self.assertIs(grid_gen.get_width, 20, "Width property is invalid")
        self.assertIs(grid_gen.get_height, 16, "Height property is invalid")

    def test_get_blocks(self):
        '''
        Check return values for differnt grids 
        '''
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'basicLayout', "")
        grid_gen.grid = list(reversed([
            ['alb', 'blb'],
            ['clb', 'dlb']
        ]))
        self.assertTupleEqual(grid_gen.get_block(0, 0), ("clb", 0, 0))
        self.assertTupleEqual(grid_gen.get_block(1, 1), ("blb", 1, 1))

        grid_gen.grid = list(reversed([
            ['alb', grid_gen.UP_ARROW],
            ['clb', 'dlb']
        ]))
        self.assertTupleEqual(grid_gen.get_block(1, 0), ("dlb", 1, 0))
        self.assertTupleEqual(grid_gen.get_block(1, 1), ("dlb", 1, 0))

        grid_gen.grid = list(reversed([
            ['alb',             'blb', "mlb"],
            [grid_gen.UP_ARROW, grid_gen.UP_ARROW, 'mlb'],
            ['clb',             grid_gen.RIGHT_ARROW, 'mlb']
        ]))
        self.assertTupleEqual(grid_gen.get_block(0, 0), ("clb", 0, 0))
        self.assertTupleEqual(grid_gen.get_block(1, 0), ("clb", 0, 0))
        self.assertTupleEqual(grid_gen.get_block(0, 1), ("clb", 0, 0))
        self.assertTupleEqual(grid_gen.get_block(1, 1), ("clb", 0, 0))
