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


    def test_enumurate_grid_basiclayout(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'basicLayout', "")
        expected_outcome = [['EMPTY', 'io_bottom', 'io_bottom', 'io_bottom', 'io_bottom', 'io_bottom', 'io_bottom', 'io_bottom', 'io_bottom', 'io_bottom', 'io_bottom', 'io_bottom', 'io_bottom', 'io_bottom', 'io_bottom', 'EMPTY'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'dsp', '→', 'dsp', '→', 'dsp', '→', 'dsp', '→', 'dsp', '→', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'ram9k', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'clb', 'io_right'], ['EMPTY', 'io_top', 'io_top', 'io_top', 'io_top', 'io_top', 'io_top', 'io_top', 'io_top', 'io_top', 'io_top', 'io_top', 'io_top', 'io_top', 'io_top', 'EMPTY']]
        outcome = [ele for ele in grid_gen.enumerate_grid()]
        self.assertEqual(outcome , expected_outcome)

    def test_enumurate_grid_smallLayout(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallLayout', "")

        expected_outcome = [['EMPTY', 'io_bottom', 'io_bottom', 'EMPTY'], ['io_left', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'io_right'], ['EMPTY', 'io_top', 'io_top', 'EMPTY']]

        outcome = [ele for ele in grid_gen.enumerate_grid()]
        self.assertEqual(outcome , expected_outcome)


    def test_enumurate_grid_smallHetroLayout(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        expected_outcome = [['EMPTY', 'io_bottom', 'io_bottom', 'EMPTY'], ['io_left', 'clb', 'clb', 'io_right'], ['io_left', 'clb', 'clb', 'io_right'], ['EMPTY', 'io_top', 'io_top', 'EMPTY']]

        outcome = [ele for ele in grid_gen.enumerate_grid()]
        self.assertEqual(outcome , expected_outcome)   


    def test_add_fill(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        tree = ET.Element ("fill", attrib={'type': "clb"})

        grid_gen.add_fill(tree)

        for yi in range(0, grid_gen.height):
            for xi in range(0, grid_gen.width):
                self.assertTupleEqual(grid_gen.get_block(yi, xi), ("clb", yi, xi))
                              

    def test_add_single(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element ("single", attrib={'type': "dsp", "x": 1, "y": 1 })
        grid_gen.add_single(tree)

        self.assertTupleEqual(grid_gen.get_block(0, 0), ("dsp", 0, 0))
        self.assertTupleEqual(grid_gen.get_block(1, 0), ("dsp", 0, 0))


    def test_add_corners(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element ("corners", attrib={'type': "clb"})
        grid_gen.add_corners(tree)

        for x in range(0, grid_gen.width, 3):
            for y in range(0, grid_gen.height, 3):
                self.assertTupleEqual(grid_gen.get_block(x, y), ("clb", x, y))

    
    def test_add_perimeter(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element ("perimeter", attrib={'type': "clb"})
        grid_gen.add_perimeter(tree)

        for yi in range(0, grid_gen.height):
            for xi in range(0, grid_gen.width):
                self.assertTupleEqual(grid_gen.get_block(yi, xi), ("clb", yi, xi)) 

    def test_add_row(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element ("row", attrib={'type': "io_right","starty": "H-1",  "startx": "W-4"})
        grid_gen.add_row(tree)

        for x in range(grid_gen.width):
            self.assertTupleEqual(grid_gen.get_block(x, 3), ("io_right", x, 3))


    def test_add_row_repeat(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element ("row", attrib={'type': "io_right","starty": "H-4",  "startx": "W-4", "repeaty":"H-2"})
        grid_gen.add_row(tree)

        for x in range(grid_gen.width):
            for y in [0, 2]:
                self.assertTupleEqual(grid_gen.get_block(x, y), ("io_right", x, y))

    def test_add_row_incr(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element ("row", attrib={'type': "io_right","starty": "H-4",  "startx": "W-4","incrx":"W-2", "repeaty":"H-2"})
        grid_gen.add_row(tree)

        for x in [0,2]:
            for y in [0, 2]:
                self.assertTupleEqual(grid_gen.get_block(x, y), ("io_right", x, y))
    

    def test_add_col(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element ("col", attrib={'type': "io_left", "startx": "W-1", "starty": "H-4"})
        grid_gen.add_col(tree)

        for y in range(grid_gen.height):
            self.assertTupleEqual(grid_gen.get_block(3, y), ("io_left", 3, y))


    def test_add_col_repeat(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element ("col", attrib={'type': "io_left", "startx": "W-4", "starty": "H-4", "repeatx": "W-2"})
        grid_gen.add_col(tree)

        for x in [0, 2]:
            for y in range(grid_gen.height):
                self.assertTupleEqual(grid_gen.get_block(x, y), ("io_left", x, y))


    def test_add_col_incr(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element ("col", attrib={'type': "io_left", "startx": "W-4", "starty": "H-4", "incry": "H-2", "repeatx": "W-2"})

        grid_gen.add_col(tree)

        for x in [0, 2]:
            for y in [0, 2]:
                self.assertTupleEqual(grid_gen.get_block(x, y), ("io_left", x, y))

    
    def test_add_region_default(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element("region",  attrib = {"type":"dsp"})

        grid_gen.add_region(tree)

        for xi in range(0, grid_gen.width, 2):
            for yi in range(0, grid_gen.height, 2):
                self.assertTupleEqual(grid_gen.get_block(xi, yi), ("dsp", xi, yi))

        for xi in range(1, grid_gen.width, 2):
            for yi in range(1, grid_gen.height, 2):
                self.assertTupleEqual(grid_gen.get_block(xi, yi), ("dsp", xi-1, yi))       
    

    def test_add_region_start_xy(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'smallHetroLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element("region",  attrib = {"type":"dsp", "startx": "W-(W-1)", "endx": "W-1", "starty":"H-(H-1)", "endy":"H-1"})

        grid_gen.add_region(tree)

        for xi in range(1, grid_gen.width-1, 2):
            for yi in range(1, grid_gen.height-1, 2):
                self.assertTupleEqual(grid_gen.get_block(xi, yi), ("dsp", xi, yi))

        for xi in range(2, grid_gen.width-1, 2):
            for yi in range(2, grid_gen.height-1, 2):
                self.assertTupleEqual(grid_gen.get_block(xi, yi), ("dsp", xi-1, yi))    

    def test_add_region_start_repeat(self):
        grid_gen = FPGAGridGen("myDesign", self.vprArchTree, 'basicLayout', "")

        grid_gen.enumerate_grid()

        tree = ET.Element("region",  attrib = {"type":"dsp", "startx": "W-(W-1)", "endx": "W-(W-4)", "repeatx": "W-6", "starty":"H-(H-1)", "endy":"H-(H-4)","repeaty": "H-5"})

        grid_gen.add_region(tree)

        for xi in [1, 3, 11, 13]:
            for yi in [1, 2, 3, 16, 17, 18]:
                self.assertTupleEqual(grid_gen.get_block(xi, yi), ("dsp", xi, yi))

        for xi in [2, 4, 12, 14]:
            for yi in [1, 2, 3, 16, 17, 18]:
                self.assertTupleEqual(grid_gen.get_block(xi, yi), ("dsp", xi-1, yi))    



