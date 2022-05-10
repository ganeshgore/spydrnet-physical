from random import randint, random
import tempfile
import unittest
import xml.etree.ElementTree as ET
import random
import spydrnet as sdn
from spydrnet_physical.ir.element import Element
from spydrnet_physical.util import FPGAGridGen, OpenFPGA_Arch, FPGAGridGen


class TestFpgaGridGen(unittest.TestCase):
    """
    """

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
                    <corners type="EMPTY" priority="101"/>
                    <fill type="clb" priority="10"/>
                    <region type="dsp" startx="3" endx="W-3" starty="H/2" incry="H" priority="30"/>
                    <region type="ram9k" startx="3" endx="W-3" starty="5" incry="5" priority="20"/>
                </fixed_layout>
                <fixed_layout name="smallLayout" width="4" height="4">
                    <row type="io_top" starty="H-1" priority="100"/>
                    <row type="io_bottom" starty="0" priority="100"/>
                    <col type="io_left" startx="0" priority="100"/>
                    <col type="io_right" startx="W-1" priority="100"/>
                    <corners type="EMPTY" priority="101"/>
                    <fill type="clb" priority="10"/>
                </fixed_layout>
                <fixed_layout name="smallHetroLayout" width="4" height="4">
                    <row type="io_top" starty="H-1" priority="100"/>
                    <row type="io_bottom" starty="0" priority="100"/>
                    <col type="io_left" startx="0" priority="100"/>
                    <col type="io_right" startx="W-1" priority="100"/>
                    <corners type="EMPTY" priority="101"/>
                    <fill type="clb" priority="10"/>
                    <single type="dsp" x="1" y="1" priority="10"/>
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

        self.assertIs(grid_gen.get_width(), 14, "Width property is invalid")
        self.assertIs(grid_gen.get_height(), 18, "Height property is invalid")

    def test_get_top_instance(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallLayout', "")
        grid_gen.enumerate_grid()
        self.assertEqual(grid_gen.width, 4)
        self.assertEqual(grid_gen.height, 4)

        expected_full_grid = list(reversed([
            ['EMPTY', 'EMPTY', 'io_top_1__2_', 'top',
                'io_top_2__2_', 'EMPTY', 'EMPTY'],
            ['EMPTY', 'sb_0__2_', 'cbx_1__2_', 'sb_1__2_',
                'cbx_2__2_', 'sb_2__2_', 'EMPTY'],
            ['io_left_0__2_', 'cby_0__2_', 'clb_1__2_', 'cby_1__2_',
                'clb_2__2_',  'cby_2__2_', 'io_right_2__2_'],
            ['EMPTY', 'sb_0__1_', 'cbx_1__1_', 'sb_1__1_',
                'cbx_2__1_', 'sb_2__1_', 'EMPTY'],
            ['io_left_0__1_', 'cby_0__1_', 'clb_1__1_',  'cby_1__1_',
                'clb_2__1_', 'cby_2__1_', 'io_right_2__1_'],
            ['EMPTY', 'sb_0__0_', 'cbx_1__0_', 'sb_1__0_',
                'cbx_2__0_', 'sb_2__0_', 'EMPTY'],
            ['EMPTY', 'EMPTY', 'io_bottom_1__0_', 'EMPTY',
                'io_bottom_2__0_', 'EMPTY', 'EMPTY']
        ]))
        for yi in range(0, grid_gen.height):
            for xi in range(0, grid_gen.width):
                self.assertEqual(
                    grid_gen.get_top_instance(xi, yi),
                    expected_full_grid[yi][xi])

    def test_get_block_size(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'basicLayout', "")

    def test_print_grid(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'basicLayout', "")
        grid_gen.grid = list(reversed([
            ['alb', 'blb'],
            ['clb', 'dlb']
        ]))
        self.assertEqual(grid_gen.print_grid(),
                         f"{'alb':^10} {'blb':^10} \n" +
                         f"{'clb':^10} {'dlb':^10} \n")

        grid_gen.grid = list(reversed([
            ['alb', 'blb'],
            ['clb', '']
        ]))
        self.assertEqual(grid_gen.print_grid(),
                         f"{'alb':^10} {'blb':^10} \n" +
                         f"{'clb':^10} {'':^10} \n")

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
