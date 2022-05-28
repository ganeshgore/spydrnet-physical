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

* ``GRID_X``
* ``GRID_Y``
* ``CLB_W``
* ``CLB_H``
* ``CBX_WIDTH``
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
import os
import json
import pandas as pd
from pprint import pformat, pprint
from spydrnet_physical.util.shell import launch_shell
from spydrnet_physical.util import GridFloorplanGen
from spydrnet_physical import PROP

import yaml
from spydrnet_physical.util import OpenFPGA_Placement_Generator, FPGAGridGen

logger = logging.getLogger('spydrnet_logs')

AREA, WIDTH, HEIGHT = 0, 1, 2
# CPP = 14
# SCALE = 100
# SC_HEIGHT = 90


class initial_hetero_placement(OpenFPGA_Placement_Generator):

    CPP = 2
    """int: ``Contated-poly-pitch`` (`default`=2) """

    SC_HEIGHT = 10
    """int: ``Standard cell height`` (`default`=10) """

    SCALE = 100
    """int: Module level variable documented inline. (`default`=100) """

    module_shapes = []
    """dict: Stores module database"""

    shaping_parameters = {}
    """dict: All the shaping paramteres """

    def __init__(self, grid, netlist, fpga_grid: FPGAGridGen, debug=False,
                 areaFile=None, shapingConf=None):
        super().__init__(grid, netlist, fpga_grid)
        self.get_default_configuration()

    def update_placement(self):
        pass

    def create_placement(self):
        """
        Overrides the base method to create placement information
        """
        # Shape the Modules
        for eachm, param in self.module_shapes.items():
            if param:
                try:
                    module = next(self._top_module.get_definitions(eachm))
                except StopIteration:
                    logger.exception('Not found %s', eachm)
                    return
                shape = param.get("SHAPE", "rect")
                if (shape == "cross") or (shape == "custom"):
                    module.data[PROP]["SHAPE"] = param["SHAPE"]
                    module.data[PROP]["POINTS"] = param["POINTS"]
                    module.data[PROP]["WIDTH"] = \
                        sum([param["POINTS"][i] for i in [1, 3, 4]])
                    module.data[PROP]["HEIGHT"] = \
                        sum([param["POINTS"][i] for i in [0, 2, 5]])
                else:
                    module.data[PROP]["SHAPE"] = 'rect'
                    module.data[PROP]["WIDTH"] = param["POINTS"][0]
                    module.data[PROP]["HEIGHT"] = param["POINTS"][1]

        # Adjusting placement grids
        self.design_grid.offset_x = (20*self.CPP)
        self.design_grid.offset_y = (2*self.SC_HEIGHT)

        # Set grid_clb column
        for i in range(2, (self.fpga_size[0]*2)+1, 2):
            self.design_grid.set_column_width(
                i, self.module_shapes["grid_clb"]["POINTS"][0])
        # Set grid_clb row
        for i in range(2, (self.fpga_size[1]*2)+1, 2):
            self.design_grid.set_row_height(
                i, self.module_shapes["grid_clb"]["POINTS"][1])

        for i in range(1, (self.fpga_size[0]*2)+2, 2):
            self.design_grid.set_column_width(
                i, self.module_shapes["cby_1__1_"]["POINTS"][0])

        for i in range(1, (self.fpga_size[1]*2)+2, 2):
            self.design_grid.set_row_height(
                i, self.module_shapes["cbx_1__1_"]["POINTS"][1])

        # Perform placement
        top_module = self._top_module
        for x_indx in range((self.fpga_size[0]*2) + 1, 0, -1):
            for y_indx in range((self.fpga_size[0]*2) + 1, 0, -1):
                x_offset, y_offset = 0, 0
                inst_name = self.fpga_grid.get_top_instance(x_indx, y_indx)
                points = self.design_grid.get_x_y(x_indx-1, y_indx-1)
                try:
                    inst = next(top_module.get_instances(f"*{inst_name}"))
                except StopIteration:
                    logger.warning("Skipping placment : %s [Not found] ",
                                   inst_name)

                module = self.module_shapes[inst.reference.name]
                x_offset, y_offset = module["PLACEMENT"](x_indx, y_indx)
                inst.data[PROP]['LOC_X'] = points[0] + x_offset
                inst.data[PROP]['LOC_Y'] = points[1] + y_offset
                # print(f"Placing {inst_name} at {points[0]} { points[1]}")

        top_module.data[PROP]["WIDTH"] = \
            self.design_grid.width + (40*self.CPP)
        top_module.data[PROP]["HEIGHT"] = \
            self.design_grid.height + (4*self.SC_HEIGHT)

    def update_configuration(self, update_module_shapes):
        '''
        Overwrite default configuration variables
        '''
        self.module_shapes.update(update_module_shapes)

    @staticmethod
    def _get_location(x, y):
        ""
        return 0, 0

    def get_default_configuration(self):

        W = self.fpga_size[0]
        H = self.fpga_size[1]
        # Placement is called with  PLACEMENT(x, y, instance, module_shapes, variables)
        self.module_shapes = {
            f"grid_clb": {"SHAPE": "rect", "POINTS": [100, 100], "PLACEMENT": self._get_location},
            # Common connection blocks [Auto calculated]
            f"cbx_1__0_": {"SHAPE": "rect", "POINTS": [100, 50], "PLACEMENT": self._get_location},
            f"cbx_1__1_": {"SHAPE": "rect", "POINTS": [100, 50], "PLACEMENT": self._get_location},
            f"cbx_1__{H}_": {"SHAPE": "rect", "POINTS": [100, 50], "PLACEMENT": self._get_location},
            f"cby_0__1_": {"SHAPE": "rect", "POINTS": [50, 100], "PLACEMENT": self._get_location},
            f"cby_{W}__1_": {"SHAPE": "rect", "POINTS": [50, 100], "PLACEMENT": self._get_location},
            f"cby_1__1_": {"SHAPE": "rect", "POINTS": [50, 100], "PLACEMENT": self._get_location},
            # Common swith blocks [Auto calculated]
            f"sb_0__0_": {"SHAPE": "cross", "POINTS": [20, 0, 20, 20, 20, 0], "PLACEMENT": self._get_location},
            f"sb_0__1_": {"SHAPE": "cross", "POINTS": [20, 0, 20, 20, 20, 20], "PLACEMENT": self._get_location},
            f"sb_0__{H}_": {"SHAPE": "cross", "POINTS": [20, 0, 0, 20, 20, 20], "PLACEMENT": self._get_location},
            f"sb_1__0_": {"SHAPE": "cross", "POINTS": [20, 20, 20, 20, 20, 20], "PLACEMENT": self._get_location},
            f"sb_1__1_": {"SHAPE": "cross", "POINTS": [20, 20, 20, 20, 20, 20], "PLACEMENT": self._get_location},
            f"sb_1__{H}_": {"SHAPE": "cross", "POINTS": [20, 20, 20, 20, 20, 20], "PLACEMENT": self._get_location},
            f"sb_{W}__0_": {"SHAPE": "cross", "POINTS": [20, 20, 20, 20, 0, 0], "PLACEMENT": self._get_location},
            f"sb_{W}__1_": {"SHAPE": "cross", "POINTS": [20, 20, 20, 20, 0, 20], "PLACEMENT": self._get_location},
            f"sb_{W}__{H}_": {"SHAPE": "cross", "POINTS": [20, 20, 0, 20, 0, 20], "PLACEMENT": self._get_location},
        }
