"""
=================
FPGA Floorplanner
=================

This dedicated OpenFPGA floorplan shapes each block in the FPGA in a classic tiling structure. This floorplanning can is applied to homogeneous architecture out of the box, but external information may be required for heterogeneous architecture.

This floor planner is sequential. It honors utilization constraints and parameter constraints in the given order.

User defined variables

GRID_AR = 1.5

Paramater Based (*Preferred*):
------------------------------

Following figure details the various paramteres referred in this type of floorplanning

.. rst-class:: ascii

::


                  |<---------  GRID_X  --------->|
                  |                              |
        ┌───────────┐┌─────────────┐┌──────────────┐┌─────────────┐┌───────────┐  ∧
        │           ││   CBX_TOP   ││              ││             ││           │  |
        │           ││   _WIDTH    ││              ││             ││           │  | CBX_TOP_HEIGHT
        │        ┌──┘└─────────────┘└──┐        ┌──┘└─────────────┘└──┐        │  ⩒
        │        │┌───────────────────┐│        │┌───────────────────┐│        │
        └────────┘│   GRID_CLB_RATIO  │└────────┘│                   │└────────┘
        ┌────────┐│       W/H         │┌────────┐│                   │┌────────┐
        │        ││                   ││        ││                   ││        │
        │  CBY_  ││                   ││   CB_  ││                   ││  CBY_  │
        │  LEFT_ ││                   ││ HEIGHT ││                   ││ RIGHT_ │
        │ HEIGHT ││                   ││ _RATIO ││                   ││ HEIGHT │
        │        ││                   ││        ││                   ││        │
        └────────┘│                   │└────────┘│                   │└────────┘
        ┌────────┐│                   │┌────────┐│                   │┌────────┐
    ↑   │        │└───────────────────┘│        │└───────────────────┘│        │
    |   │        └──┐┌─────────────┐┌──┘        └──┐┌─────────────┐┌──┘        │
    |   │           ││  CB_WIDTH_  ││              ││             ││           │  FPGA_SIZE[0],y
    |   │           ││    RATIO    ││              ││             ││           │
    G   │        ┌──┘└─────────────┘└──┐        ┌──┘└─────────────┘└──┐        │
    R   │        │┌───────────────────┐│        │┌───────────────────┐│        │
    I   └────────┘│                   │└────────┘│                   │└────────┘
    D   ┌────────┐│                   │┌────────┐│                   │┌────────┐
    _   │        ││                   ││        ││                   ││        │
    Y   │        ││                   ││        ││                   ││        │
    |   │        ││                   ││        ││                   ││        │
    |   │        ││                   ││        ││                   ││        │
    |   │        ││                   ││        ││                   ││        │
    |   └────────┘│                   │└────────┘│                   │└────────┘
    |   ┌────────┐│                   │┌────────┐│                   │┌────────┐
    ↓   │        │└───────────────────┘│        │└───────────────────┘│        │
        │        └──┐┌─────────────┐┌──┘        └──┐┌─────────────┐┌──┘        │  ∧
        │           ││ CBX_BOTTOM_ ││              ││             ││           │  |
        │           ││   _WIDTH    ││              ││             ││           │  | CBX_BOTTOM_HEIGHT
        └───────────┘└─────────────┘└──────────────┘└─────────────┘└───────────┘  ⩒
        <----------->                                               <--------->
        CBY_LEFT_WIDTH                                           CBY_RIGHT_WIDTH


**Area Based**:

- ``OVERALL_UTILIZATION``
- ``GRID_CLB_UTILIZATION``
- ``SB_UTILIZATION``


**Common Parameters** (All of them are absolute numbers in multiple of *SC_HEIGHT* or *CPP*)

- ``GRID_CLB_CHAN_X`` and ``GRID_CLB_CHAN_Y``: Grid CLB margins
- ``CBx_CHAN_X`` and ``CBx_CHAN_Y`` : Connection box X margins
- ``CBy_CHAN_X`` and ``CBy_CHAN_Y`` : Connection box Y margins
- ``GPIO_CHAN_X`` and ``GPIO_CHAN_Y``: GPIO cell margins


**Absolute Numbers** (In multiple of *SC_HEIGHT* or *CPP*)

* ``tile_width``
* ``tile_height``
* ``CLB_W``
* ``CLB_H``
* ``CBX_WIDTH``
* ``CBX_HEIGHT``
* ``CBY_WIDTH``
* ``CBY_HEIGHT``
* ``LEFT_CBY_WIDTH``
* ``LEFT_CBY_HEIGHT``
* ``RIGHT_CBY_WIDTH``
* ``RIGHT_CBY_HEIGHT``
* ``TOP_CBX_WIDTH``
* ``TOP_CBX_HEIGHT``
* ``BOTTOM_CBX_WIDTH``
* ``BOTTOM_CBX_HEIGHT``


Utilization Based
-----------------

**Ideas**:

* Optionally provide a method to apply shaping and placement to the netlist elements

"""


import logging
import math
import json
from copy import deepcopy
from typing import Callable
from pprint import pformat, pprint
from spydrnet_physical.util.shell import launch_shell
from spydrnet_physical.util import GridFloorplanGen
from spydrnet_physical import PROP

import yaml
from spydrnet_physical.util import OpenFPGA_Placement_Generator, FPGAGridGen

logger = logging.getLogger("spydrnet_logs")

AREA, WIDTH, HEIGHT = 0, 1, 2

CBX_COLOR = "#d9d9f3"
CBY_COLOR = "#a8d0db"
SB_COLOR = "#ceefe4"
GRID_COLOR = "#ddd0b1"


class initial_hetero_placement(OpenFPGA_Placement_Generator):

    CPP = 2
    """int: ``Contated-poly-pitch`` (`default`=2) """

    SC_HEIGHT = 10
    """int: ``Standard cell height`` (`default`=10) """

    SCALE = 100
    """int: Module level variable documented inline. (`default`=100) """

    margins = {}
    """dict: Stores module database without any margin"""

    module_shapes_final = {}
    """dict: Stores module database without any margin"""

    module_final = {}
    """dict: Stores module database with margin"""

    s_param = {
        "TILE_ASPECT_RATIO": 1,
        "OFFSET_X": 20,
        "OFFSET_Y": 2,
    }
    """dict: All the shaping paramteres """

    def __init__(
        self,
        grid,
        netlist,
        fpga_grid: FPGAGridGen,
        debug=False,
        areaFile=None,
        shapingConf=None,
    ):
        super().__init__(grid, netlist, fpga_grid)
        self.SC_GRID = self.SC_HEIGHT * self.CPP
        self.calculate_shapes()
        self.create_shapes()
        self.add_module_colors()

    def add_module_colors(self):
        for cbx in self._top_module.get_definitions("cbx_*"):
            cbx.data[PROP]["COLOR"] = CBX_COLOR

        for cby in self._top_module.get_definitions("cby_*"):
            cby.data[PROP]["COLOR"] = CBY_COLOR

        for sb in self._top_module.get_definitions("sb_*"):
            sb.data[PROP]["COLOR"] = SB_COLOR

        for grid in self._top_module.get_definitions("grid_*"):
            grid.data[PROP]["COLOR"] = GRID_COLOR

    def update_placement(self):
        pass

    def create_placement(self):
        """
        Overrides the base method to create placement information
        """
        self.update_shapes()

        # Perform placement
        top_module = self._top_module
        for x_indx in range((self.fpga_size[0] * 2) + 1, 0, -1):
            for y_indx in range((self.fpga_size[1] * 2) + 1, 0, -1):
                x_off, y_off = 0, 0
                inst_name = self.fpga_grid.get_top_instance(x_indx, y_indx)
                anchor = self.design_grid.get_x_y(x_indx - 1, y_indx - 1)
                try:
                    inst = next(top_module.get_instances(f"*{inst_name}"))
                except StopIteration:
                    logger.warning("Skipping placment : %s [Not found]", inst_name)
                module = self.module_shapes[inst.reference.name]
                if isinstance(module["PLACEMENT"], Callable):
                    x_off, y_off = module["PLACEMENT"](x_indx, y_indx)
                if isinstance(module["PLACEMENT"], tuple):
                    x_off, y_off = module["PLACEMENT"]
                if isinstance(module["PLACEMENT"], list):
                    x_off, y_off = module["PLACEMENT"]
                inst.data[PROP]["LOC_X"] = math.floor(anchor[0] + (x_off * self.CPP))
                inst.data[PROP]["LOC_Y"] = math.floor(
                    anchor[1] + (y_off * self.SC_HEIGHT)
                )

        top_module.data[PROP]["WIDTH"] = self.design_grid.width + (
            2 * self.s_param["OFFSET_X"] * self.CPP
        )
        top_module.data[PROP]["HEIGHT"] = self.design_grid.height + (
            2 * self.s_param["OFFSET_Y"] * self.SC_HEIGHT
        )

    def update_placement_grid(self):
        """
        Update two dimensional placement grid
        """
        # Adjusting placement grids
        self.design_grid.offset_x = self.s_param["OFFSET_X"] * self.CPP
        self.design_grid.offset_y = self.s_param["OFFSET_Y"] * self.SC_HEIGHT

        W = self.fpga_size[0]
        H = self.fpga_size[1]

        # Set grid_clb column
        for i in range(2, (self.fpga_size[0] * 2) + 1, 2):
            self.design_grid.set_column_width(i, self.s_param["clb_w"] * self.CPP)
        # Set grid_clb row
        for i in range(2, (self.fpga_size[1] * 2) + 1, 2):
            self.design_grid.set_row_height(i, self.s_param["clb_h"] * self.SC_HEIGHT)

        for i in range(1, (self.fpga_size[0] * 2) + 2, 2):
            self.design_grid.set_column_width(i, self.s_param["cby11_w"] * self.CPP)

        for i in range(1, (self.fpga_size[1] * 2) + 2, 2):
            self.design_grid.set_row_height(i, self.s_param["cbx11_h"] * self.SC_HEIGHT)

        self.design_grid.set_row_height(
            1, self.s_param["bottom_cbx_h"] * self.SC_HEIGHT
        )
        self.design_grid.set_row_height(-1, self.s_param["top_cbx_h"] * self.SC_HEIGHT)
        self.design_grid.set_column_width(1, self.s_param["left_cby_w"] * self.CPP)
        self.design_grid.set_column_width(-1, self.s_param["right_cby_w"] * self.CPP)

    def update_shapes(self):
        """
        This method updates the shape of all the modules based on the
        s_params variable
        """
        for eachm, param in self.module_shapes.items():
            if not param:
                continue
            try:
                module = next(self._top_module.get_definitions(eachm))
            except StopIteration:
                logger.exception("Not found %s", eachm)
                return
            shape = param.get("SHAPE", "rect")
            if (shape == "cross") or (shape == "custom"):
                points = self._scale_shape(shape, param["POINTS"])
                module.data[PROP]["SHAPE"] = shape
                module.data[PROP]["POINTS"] = points
                module.data[PROP]["WIDTH"] = sum(
                    [param["POINTS"][i] for i in [1, 3, 4]]
                )
                module.data[PROP]["HEIGHT"] = sum(
                    [param["POINTS"][i] for i in [0, 2, 5]]
                )
            else:
                module.data[PROP]["SHAPE"] = "rect"
                module.data[PROP]["WIDTH"] = param["POINTS"][0] * self.CPP
                module.data[PROP]["HEIGHT"] = param["POINTS"][1] * self.SC_HEIGHT

    def _scale_shape(self, shape, points):
        if shape == "cross":
            points = [
                a * b
                for a, b in (
                    zip(
                        points,
                        (
                            self.SC_HEIGHT,
                            self.CPP,
                            self.SC_HEIGHT,
                            self.CPP,
                            self.CPP,
                            self.SC_HEIGHT,
                        ),
                    )
                )
            ]
        if shape == "custom":
            pass
        return points

    def update_shaping_param(self, update_module_shapes):
        """
        Overwrite default configuration variables
        """
        self.s_param.update(update_module_shapes)

    @staticmethod
    def _get_location(x, y):
        """"""
        return 0, 0

    @staticmethod
    def base2(number, multiple=2):
        """Snaps the point in multiple for 2"""
        return multiple * round(number / multiple)

    @staticmethod
    def base4(number, multiple=4):
        """Snaps the point in multiple for 4"""
        return multiple * round(number / multiple)

    def _get_width_height(self, area, aspect_ratio=1, width=None, height=None):
        """
        Return the width and height given the area anad aspect ratio

        if any fixed values is provides (like width and height) other values is
        calculated without honoring aspect ratio

        Args:
            area (float):
            aspect_ratio (float):
            width (float):
            height (float):

        Return:
            (flota, float)
        """
        area_um = area * self.SC_GRID
        if width is None and height is None:
            height_um = int(math.sqrt(area_um / aspect_ratio))
            width_um = int(area_um / height_um)
        elif width:
            width_um = width * self.CPP
            height_um = int(area_um / width_um)
        elif height:
            height_um = height * self.SC_HEIGHT
            width_um = int(area_um / height_um)
        width = self.base2(width_um / self.CPP)
        height = self.base2(height_um / self.SC_HEIGHT)
        return width, height

    def get_area(self, module):
        """
        Return the area of the given module after considering the utilisation
        """
        module_inst = next(self._top_module.get_definitions(module))
        area = module_inst.data[PROP]["AREA"]
        area *= 1 / self.s_param[f"{module}_util"]
        return area

    def calculate_shapes(self):
        """
        This function compute different base variable for shaping FPGA fabric
        """
        m = self.s_param
        for each_module in self._top_module.get_definitions("*"):
            m[f"{each_module.name}_util"] = 0.85

        # TODO : Need to genrate these parameters automatically
        m["clb_w"], m["clb_h"] = 100, 20

        m["cbx11_w"], m["cbx11_h"] = 60, 6
        m["bottom_cbx_w"], m["bottom_cbx_h"] = 70, 10
        m["top_cbx_w"], m["top_cbx_h"] = 70, 10

        m["cby11_w"], m["cby11_h"] = 30, 12
        m["left_cby_w"], m["left_cby_h"] = 40, 16
        m["right_cby_w"], m["right_cby_h"] = 40, 16

        self.derive_sb_paramters()

    def derive_sb_paramters(self):
        """
        This method calculated switch block dimensions from grid_clb and cb
        """

        m = self.s_param

        # Dervived calcualation
        # Center switch box
        m["a"] = math.floor(m["cbx11_h"])
        m["b"] = math.floor(0.5 * (m["clb_w"] - m["cbx11_w"]))
        m["c"] = math.floor(0.5 * (m["clb_h"] - m["cby11_h"]))
        m["d"] = math.floor(m["cby11_w"])
        m["e"] = math.floor(0.5 * (m["clb_w"] - m["cbx11_w"]))
        m["f"] = math.floor(0.5 * (m["clb_h"] - m["cby11_h"]))

        # Left switch block dimensions
        m["la"] = math.floor(m["cbx11_h"])
        m["lb"] = math.floor(0)
        m["lc"] = math.floor(0.5 * (m["clb_h"] - m["left_cby_h"]))
        m["ld"] = math.floor(m["left_cby_w"])
        m["le"] = math.floor(0.5 * (m["clb_w"] - m["cbx11_w"]))
        m["lf"] = math.floor(0.5 * (m["clb_h"] - m["left_cby_h"]))

        # Right switch block dimensions
        m["ra"] = math.floor(m["cbx11_h"])
        m["rb"] = math.floor(0.5 * (m["clb_w"] - m["cbx11_w"]))
        m["rc"] = math.floor(0.5 * (m["clb_h"] - m["right_cby_h"]))
        m["rd"] = math.floor(m["right_cby_w"])
        m["re"] = math.floor(0)
        m["rf"] = math.floor(0.5 * (m["clb_h"] - m["right_cby_h"]))

        # Top switch block dimensions
        m["ta"] = math.floor(m["top_cbx_h"])
        m["tb"] = math.floor(0.5 * (m["clb_w"] - m["top_cbx_w"]))
        m["tc"] = math.floor(0)
        m["td"] = math.floor(m["cby11_w"])
        m["te"] = math.floor(0.5 * (m["clb_w"] - m["top_cbx_w"]))
        m["tf"] = math.floor(0.5 * (m["clb_h"] - m["cby11_h"]))

        # Bottom switch block dimensions
        m["ba"] = math.floor(m["bottom_cbx_h"])
        m["bb"] = math.floor(0.5 * (m["clb_w"] - m["bottom_cbx_w"]))
        m["bc"] = math.floor(0.5 * (m["clb_h"] - m["cby11_h"]))
        m["bd"] = math.floor(m["cby11_w"])
        m["be"] = math.floor(0.5 * (m["clb_w"] - m["bottom_cbx_w"]))
        m["bf"] = math.floor(0)
        self.update_placement_grid()

    def create_shapes(self):
        m = self.s_param

        W = self.fpga_size[0]
        H = self.fpga_size[1]
        # Placement is called with  PLACEMENT(x, y, instance, module_shapes, variables)
        self.module_shapes = {
            "grid_clb": {
                "SHAPE": "rect",
                "POINTS": [m["clb_w"], m["clb_h"]],
                "PLACEMENT": [0, 0],
            },
            # Common connection blocks [Auto calculated]
            "cbx_1__0_": {
                "SHAPE": "rect",
                "POINTS": [m["bottom_cbx_w"], m["bottom_cbx_h"]],
                "PLACEMENT": [0.5 * (m["clb_w"] - m["bottom_cbx_w"]), 0],
            },
            "cbx_1__1_": {
                "SHAPE": "rect",
                "POINTS": [m["cbx11_w"], m["cbx11_h"]],
                "PLACEMENT": [0.5 * (m["clb_w"] - m["cbx11_w"]), 0],
            },
            f"cbx_1__{H}_": {
                "SHAPE": "rect",
                "POINTS": [m["top_cbx_w"], m["top_cbx_h"]],
                "PLACEMENT": [0.5 * (m["clb_w"] - m["top_cbx_w"]), 0],
            },
            "cby_0__1_": {
                "SHAPE": "rect",
                "POINTS": [m["left_cby_w"], m["left_cby_h"]],
                "PLACEMENT": [0, 0.5 * (m["clb_h"] - m["left_cby_h"])],
            },
            f"cby_{W}__1_": {
                "SHAPE": "rect",
                "POINTS": [m["right_cby_w"], m["right_cby_h"]],
                "PLACEMENT": [0, 0.5 * (m["clb_h"] - m["right_cby_h"])],
            },
            "cby_1__1_": {
                "SHAPE": "rect",
                "POINTS": [m["cby11_w"], m["cby11_h"]],
                "PLACEMENT": [0, 0.5 * (m["clb_h"] - m["cby11_h"])],
            },
            # Common swith blocks [Auto calculated]
            "sb_0__0_": {
                "SHAPE": "cross",
                "POINTS": [m["ba"], 0, m["lc"], m["ld"], m["be"], 0],
                "PLACEMENT": [0, 0],
            },
            "sb_0__1_": {
                "SHAPE": "cross",
                "POINTS": [m["la"], m["lb"], m["lc"], m["ld"], m["le"], m["lf"]],
                "PLACEMENT": [0, -0.5 * (m["clb_h"] - m["left_cby_h"])],
            },
            f"sb_0__{H}_": {
                "SHAPE": "cross",
                "POINTS": [m["ta"], 0, 0, m["ld"], m["te"], m["lf"]],
                "PLACEMENT": [0, -0.5 * (m["clb_h"] - m["left_cby_h"])],
            },
            "sb_1__0_": {
                "SHAPE": "cross",
                "POINTS": [m["ba"], m["bb"], m["bc"], m["bd"], m["be"], m["bf"]],
                "PLACEMENT": [-0.5 * (m["clb_w"] - m["bottom_cbx_w"]), 0],
            },
            "sb_1__1_": {
                "SHAPE": "cross",
                "POINTS": [m["a"], m["b"], m["c"], m["d"], m["e"], m["f"]],
                "PLACEMENT": [
                    -0.5 * (m["clb_w"] - m["cbx11_w"]),
                    -0.5 * (m["clb_h"] - m["cby11_h"]),
                ],
            },
            f"sb_1__{H}_": {
                "SHAPE": "cross",
                "POINTS": [m["ta"], m["tb"], m["tc"], m["td"], m["te"], m["tf"]],
                "PLACEMENT": [
                    -0.5 * (m["clb_w"] - m["top_cbx_w"]),
                    -0.5 * (m["clb_h"] - m["cby11_h"]),
                ],
            },
            f"sb_{W}__0_": {
                "SHAPE": "cross",
                "POINTS": [m["ba"], m["bb"], m["rc"], m["rd"], 0, 0],
                "PLACEMENT": [-0.5 * (m["clb_w"] - m["bottom_cbx_w"]), 0],
            },
            f"sb_{W}__1_": {
                "SHAPE": "cross",
                "POINTS": [m["ra"], m["rb"], m["rc"], m["rd"], m["re"], m["rf"]],
                "PLACEMENT": [
                    -0.5 * (m["clb_w"] - m["cbx11_w"]),
                    -0.5 * (m["clb_h"] - m["right_cby_h"]),
                ],
            },
            f"sb_{W}__{H}_": {
                "SHAPE": "cross",
                "POINTS": [m["ta"], m["tb"], 0, m["rd"], 0, m["rf"]],
                "PLACEMENT": [
                    -0.5 * (m["clb_w"] - m["top_cbx_w"]),
                    -0.5 * (m["clb_h"] - m["right_cby_h"]),
                ],
            },
        }
