""" Tst cases fro get_names method """
from spydrnet_physical.util import OpenFPGA, Tile01
import spydrnet as sdn
from os.path import abspath
from itertools import chain
import tempfile
import glob
import unittest
from spydrnet_physical.util import get_names


class TestOpenFPGA(unittest.TestCase):
    """Test case to cehck OpenFPGA"""

    def setUp(self) -> None:
        self.source_dir = abspath("examples/homogeneous_fabric")
        source_files = glob.glob(f"{self.source_dir}/*_Verilog/lb/*.v")
        source_files += glob.glob(f"{self.source_dir}/*_Verilog/routing/*.v")
        source_files += glob.glob(f"{self.source_dir}/*_Verilog/sub_module/*.v")
        source_files += glob.glob(f"{self.source_dir}/*_Verilog/fpga_top.v")

        # Create OpenFPGA object
        self.fpga = OpenFPGA(grid=(4, 4), verilog_files=source_files)

        # Convert wires to bus structure
        self.fpga.create_grid_clb_bus()
        self.fpga.create_grid_io_bus()
        self.fpga.create_sb_bus()
        self.fpga.create_cb_bus()

        # Remove undriven nets
        self.fpga.remove_undriven_nets()

        # Top level nets to bus
        for i in chain(
            self.fpga.top_module.get_instances("grid_clb*"),
            self.fpga.top_module.get_instances("grid_io*"),
            self.fpga.top_module.get_instances("sb_*"),
        ):
            for p in filter(lambda x: True, i.reference.ports):
                if p.size > 1 and (i.check_all_scalar_connections(p)):
                    cable_list = []
                    for pin in p.pins[::-1]:
                        cable_list.append(i.pins[pin].wire.cable)
                    self.fpga.top_module.combine_cables(
                        f"{i.name}_{p.name}", cable_list
                    )

        self.fpga.create_grid_clb_feedthroughs()

    @unittest.skip(reason="Replace this with unit test")
    def test_grid_clb_ports(self):
        """Verify grid clb port names"""
        clb = next(self.fpga.library.get_definitions("grid_clb"))

        port_names = get_names(clb.get_ports())

        self.assertIn("grid_top_in", port_names)
        self.assertIn("grid_top_out", port_names)
        self.assertIn("grid_bottom_in", port_names)
        self.assertIn("grid_bottom_out", port_names)
        self.assertIn("grid_left_in", port_names)
        self.assertIn("grid_left_out", port_names)
        self.assertIn("grid_right_in", port_names)
        self.assertIn("grid_right_out", port_names)

    @unittest.skip(reason="Replace this with unit test")
    def test_cbx11_ports(self):
        """Verify grid clb port names"""
        cbx11 = next(self.fpga.library.get_definitions("cbx_1__1_"))

        cbx11_names = get_names(cbx11.get_ports())

        # grid pins
        self.assertIn("grid_top_in", cbx11_names)
        self.assertIn("grid_top_out", cbx11_names)
        self.assertIn("grid_bottom_in", cbx11_names)
        self.assertIn("grid_bottom_out", cbx11_names)
        # Channel routing
        self.assertIn("chanx_left_in", cbx11_names)
        self.assertIn("chanx_left_out", cbx11_names)
        self.assertIn("chanx_right_in", cbx11_names)
        self.assertIn("chanx_right_out", cbx11_names)
        # grid out
        self.assertIn("grid_left_t_out", cbx11_names)
        self.assertIn("grid_left_b_out", cbx11_names)
        self.assertIn("grid_right_t_out", cbx11_names)
        self.assertIn("grid_right_b_out", cbx11_names)

    @unittest.skip(reason="Replace this with unit test")
    def test_cby11_ports(self):
        """Verify grid clb port names"""
        cby11 = next(self.fpga.library.get_definitions("cby_1__1_"))

        cby11_names = get_names(cby11.get_ports())

        # grid pins
        self.assertIn("grid_left_in", cby11_names)
        self.assertIn("grid_left_out", cby11_names)
        self.assertIn("grid_right_in", cby11_names)
        self.assertIn("grid_right_out", cby11_names)
        # Channel routing
        self.assertIn("chany_top_in", cby11_names)
        self.assertIn("chany_top_out", cby11_names)
        self.assertIn("chany_bottom_in", cby11_names)
        self.assertIn("chany_bottom_out", cby11_names)
        # grid out
        self.assertIn("grid_top_l_out", cby11_names)
        self.assertIn("grid_top_r_out", cby11_names)
        self.assertIn("grid_bottom_l_out", cby11_names)
        self.assertIn("grid_bottom_r_out", cby11_names)

    @unittest.skip(reason="Replace this with unit test")
    def test_sb11_ports(self):
        """Verify grid clb port names"""
        sb11 = next(self.fpga.library.get_definitions("sb_1__1_"))

        sb11_names = get_names(sb11.get_ports())

        # Channel routing
        self.assertIn("chany_top_in", sb11_names)
        self.assertIn("chany_top_out", sb11_names)
        self.assertIn("chany_bottom_in", sb11_names)
        self.assertIn("chany_bottom_out", sb11_names)
        self.assertIn("chanx_left_in", sb11_names)
        self.assertIn("chanx_left_out", sb11_names)
        self.assertIn("chanx_right_in", sb11_names)
        self.assertIn("chanx_right_out", sb11_names)
        # Grid out
        self.assertIn("grid_top_l_in", sb11_names)
        self.assertIn("grid_top_r_in", sb11_names)
        self.assertIn("grid_bottom_l_in", sb11_names)
        self.assertIn("grid_bottom_r_in", sb11_names)
        self.assertIn("grid_left_t_in", sb11_names)
        self.assertIn("grid_left_b_in", sb11_names)
        self.assertIn("grid_right_t_in", sb11_names)
        self.assertIn("grid_right_b_in", sb11_names)

    @unittest.skip(reason="Replace this with unit test")
    def test_create_tiles(self):
        self.fpga.register_tile_generator(Tile01)
        self.fpga.create_tiles()
        top_instances = self.fpga.top_module.children
        top_references = set([inst.reference.name for inst in top_instances])
        self.assertEqual(
            top_references,
            {
                "tile",
                "left_tile",
                "right_tile",
                "top_tile",
                "bottom_tile",
                "bottom_left_tile",
                "bottom_right_tile",
                "top_left_tile",
                "top_right_tile",
            },
        )
