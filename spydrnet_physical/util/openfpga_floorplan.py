"""
====================
OpenFPGA Floorplaner
====================

This is dedicated OpenFPGA floorplaner which shape tiles in traditional structure
as shown below. This placement class is not dependent iupon the architecture and always 
applied to homogeneous structure.

There are two brod categories of inputs,

**Paramater Based** (*Preferred*):

Following figure details the various paramteres referred in this class

.. rst-class:: ascii

::

                 
                |<-----  GRID_X  ----->|
                |                      |
        ┌───────────┐┌─────────────┐┌──────────────┐┌─────────────┐┌───────────┐  ∧
        │           ││   CBX_TOP   ││              ││             ││           │  | 
        │           ││   _WIDTH    ││              ││             ││           │  | CBX_TOP_HEIGHT
        │        ┌──┘└─────────────┘└──┐        ┌──┘└─────────────┘└──┐        │  ∨
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
        └───────────┘└─────────────┘└──────────────┘└─────────────┘└───────────┘  ∨
        <-------->                                                    <-------->
        CBY_LEFT_WIDTH                                           CBY_RIGHT_WIDTH


**Area Based**: 

- ``OVERALL_UTILIZATION``
- ``GRID_CLB_UTILIZATION``
- ``SB_UTILIZATION``


**Common Paramters**

- ``GRID_CLB_CHAN_X`` and ``GRID_CLB_CHAN_Y``: Grid CLB margins
- ``CBx_CHAN_X`` and ``CBx_CHAN_Y`` : Connection box X margins
- ``CBy_CHAN_X`` and ``CBy_CHAN_Y`` : Connection box Y margins
- ``GPIO_CHAN_X`` and ``GPIO_CHAN_Y``: GPIO cell margins


**Ideas**: 

* Optionally provide a method to apply shaping and placement to the netlist elements

"""


import logging
import math
import os

import pandas as pd
import yaml
from spydrnet_physical.util import OpenFPGA_Placement_Generator

logger = logging.getLogger('spydrnet_logs')

AREA, WIDTH, HEIGHT = 0, 1, 2
CPP = 4
SC_HEIGHT = 4


class openfpga_floorplan(OpenFPGA_Placement_Generator):
    """
    Extends the ``OpenFPGA_Placement_Generator`` class to OpenFPGA grid.

    args:

      grid_size(int, int) : FPGA grid size
      netlist(sdn.Netlist): Netlist of grid
      library(sdn.Library): Library of the netlist
      shapingConf(os.path): YAML/JSON file with parameter values
      areaFile(os.path):  CSV file with area information of each Module
      debug(bool): To enable debugging mode 
      gridIO(bool): To display gridIO modules
    """

    def __init__(self, grid_size, netlist, fpga_grid,
                 shapingConf=None, areaFile=None, debug=False):
        super().__init__(grid_size, netlist, fpga_grid)

        self.sizeX, self.sizeY = grid_size
        self.PlacementDB = []
        self.PlacementDBKey = {}
        self.GPIOPlacmentKey = []
        self.debug = debug
        self.fpga_grid = fpga_grid

        self.get_default_configuration()
        self.areaFile = areaFile
        self.skipChannels = False

        # Color Setting
        self.CLB_COLOR = "#f4f0e6"
        self.CBX_COLOR = "#d9d9f3"
        self.CBY_COLOR = "#a8d0db"
        self.SB_COLOR = "#ceefe4"
        self.GRID_IO_COLOR = "#ff8000"

        if shapingConf:
            self.update_default_configuration(shapingConf)

    def validate_placement(self, GRID_X, GRID_Y) -> bool:
        """
        Validates placement inforamtion genrerated 

        Checks if each instance is placed on the `GRID_X` and `GRID_Y` intersection
        Generally the values of  `GRID_X` and `GRID_Y` is `4*CPP` and `2*SC_HEIGHT`
        """
        raise NotImplementedError

    def create_placement(self):
        """
        Overrides the base method to create placement information
        """
        self.ComputeGrid(skipChannels=False)
        self.CreateDatabase()
        visited = []
        for instance_name, instance_info in self.PlacementDBKey.items():
            bbox = instance_info["bbox"]
            instance = next(self._top_module.get_instances(instance_name))
            module = instance.reference
            if len(instance_info["shape"]) == 1:
                if not module.name in visited:
                    llx, lly, w, h = instance_info["shape"][0]
                    module.properties["WIDTH"] = float(w)*CPP
                    module.properties["HEIGHT"] = float(h)*SC_HEIGHT

                instance.properties["LOC_X"] = bbox[0]*CPP
                instance.properties["LOC_Y"] = bbox[1]*SC_HEIGHT
            else:
                if not module.name in visited:
                    w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
                    module.properties["WIDTH"] = float(w)*CPP
                    module.properties["HEIGHT"] = float(h)*SC_HEIGHT
                instance.properties["LOC_X"] = bbox[0]*CPP
                instance.properties["LOC_Y"] = bbox[1]*SC_HEIGHT

        self._top_module.properties["WIDTH"] = 500*CPP
        self._top_module.properties["HEIGHT"] = 500*SC_HEIGHT

    def update_default_configuration(self, shapingConf):
        with open(shapingConf, "r") as file:
            for eachKey, eachValue in yaml.load(file, Loader=yaml.FullLoader).items():
                setattr(self, eachKey, eachValue)

    def get_default_configuration(self):
        # Grid clb shape
        self.SC_RATIO = 1  # This is SC_HEIGHT/CPP of stadard cell
        self.GRID_CLB_RATIO = 1  # This is actual dimension of the CLB unit width/height

        # Connection box size
        self.GRID_RATIO_X, self.GRID_RATIO_Y = 2, 2
        self.CBX_WIDTH_RATIO, self.CBY_HEIGHT_RATIO = 1, 1

        # Channel spacing between blocks
        self.CLB_CHAN_T, self.CLB_CHAN_B = 0, 0
        self.CLB_CHAN_L, self.CLB_CHAN_R = 0, 0

        self.CBX_CHAN_T, self.CBX_CHAN_B = 0, 0
        self.CBX_CHAN_L, self.CBX_CHAN_R = 0, 0

        self.CBY_CHAN_T, self.CBY_CHAN_B = 0, 0
        self.CBY_CHAN_L, self.CBY_CHAN_R = 0, 0

        self.gridIO_MT, self.gridIO_MB = 1, 1
        self.gridIO_ML, self.gridIO_MR = 2, 2

        self.gridIO_HT, self.gridIO_HB = 10, 10
        self.gridIO_WL, self.gridIO_WR = 10, 10

        self.GRID_IOV_H_RATIO = 1
        self.GRID_IOH_W_RATIO = 1

        # TODO: Deprecate this
        self.GPIO_CHAN_X, self.GPIO_CHAN_Y = 0, 0
        self.GPIO_WIDTH, self.GPIO_HEIGHT = 40, 8

    def get_variables(self):
        return {
            "CLB_COLOR": self.CLB_COLOR,
            "CBX_COLOR": self.CBX_COLOR,
            "CBY_COLOR": self.CBY_COLOR,
            "SB_COLOR": self.SB_COLOR,
            "GRID_IO_COLOR": self.GRID_IO_COLOR,
            "CORE_BBOX": (0, 0, int(self.CLB_GRID_X*(self.sizeX+1)),
                          int(self.CLB_GRID_Y*(self.sizeY+1)))
        }

    def snapDims(self, num, dim=2):
        return int(math.ceil(num/dim)*dim)

    def ComputeGrid(self, skipChannels=False):
        """
        Based on the strategy selected, Area_based or parameter_based 
        this method performs the complete calculation and prepares 
        all intermediate varaibles. 
        It also performs rouding based on `SC_HEIGHT` and `CPP` values
        """
        self.skipChannels = skipChannels
        if self.areaFile:
            BlockArea = {}
            for eachLine in open(self.areaFile, "r"):
                module, dims = eachLine.split(" ", 1)
                BlockArea[module] = list(map(float, list(dims.split())))
            self.CLB_DIM = BlockArea["grid_clb_1__1_"]
            self.CB_DIM = BlockArea["cbx_1__1_"]
        else:
            self.CLB_DIM = [2500, 24*8, 24]
            self.CB_DIM = [2500*0.6, 0, 0]

        # Snap CLB Height and Width to next Multiple of 2
        self.CLB_UNIT = math.sqrt(
            self.CLB_DIM[AREA]/(self.GRID_CLB_RATIO*self.SC_RATIO))

        self.CLB_H = self.snapDims(self.CLB_UNIT, 2)
        self.CLB_W = self.snapDims(self.CLB_DIM[AREA]/self.CLB_H, 2)

        self.CLB_GRID_X = self.snapDims(self.CLB_W*self.GRID_RATIO_X, 2)
        self.CLB_GRID_Y = self.snapDims(self.CLB_H*self.GRID_RATIO_Y, 2)

        self.CBX_W = self.snapDims(self.CLB_W*self.CBX_WIDTH_RATIO, 2)
        self.CBX_H = self.CLB_GRID_Y-self.CLB_H

        self.CBY_W = self.CLB_GRID_X-self.CLB_W
        self.CBY_H = self.snapDims(self.CLB_H*self.CBY_HEIGHT_RATIO, 2)

        self.SB_W = self.CLB_GRID_X - self.CBX_W
        self.SB_H = self.CLB_GRID_Y - self.CBY_H
        self.SIDE_X = self.CLB_GRID_X - self.CLB_W
        self.SIDE_Y = self.CLB_GRID_Y - self.CLB_H

        self.GRID_IOV_H = self.CLB_H*self.GRID_IOV_H_RATIO
        self.GRID_IOH_W = self.CLB_W*self.GRID_IOH_W_RATIO

        if self.debug:
            print(f"self.CLB_W {self.CLB_W}")
            print(f"self.CLB_H {self.CLB_H}")
            print(f"self.CLB_GRID_X {self.CLB_GRID_X}")
            print(f"self.CLB_GRID_Y {self.CLB_GRID_Y}")
            print(f"self.CBX_W {self.CBX_W}")
            print(f"self.CBX_H {self.CBX_H}")
            print(f"self.CBY_W {self.CBY_W}")
            print(f"self.CBY_H {self.CBY_H}")
            print(f"self.SB_W {self.SB_W}")
            print(f"self.SB_H {self.SB_H}")

    def CreateDatabase(self):
        # Create Blocks
        grid_ele_size = {}

        for x in range(self.sizeX+1):
            for y in range(self.sizeY+1):
                self.add_sb(x, y)
                if x < self.sizeX:
                    self.add_cbx(x, y)
                if y < self.sizeY:
                    self.add_cby(x, y)
                if (x < self.sizeX) and (y < self.sizeY):
                    label = self.fpga_grid[y+1][x+1]
                    if not (label in [self.grid.RIGHT_ARROW, self.grid.UP_ARROW, "EMPTY"]):
                        if not label in grid_ele_size.keys():
                            ele_w, ele_h = self.grid.fpga_arch.tiles[label]
                            grid_ele_size[label] = (ele_w, ele_h)
                        else:
                            ele_w, ele_h = grid_ele_size[label]
                        self.add_clb(x, y, width=ele_w,
                                     height=ele_h, lbl=label)

        return self.PlacementDB

    def add_clb(self, xi, yi, lbl=None):
        x, y = (xi+1)*self.CLB_GRID_X, (yi+1)*self.CLB_GRID_Y
        llx = x-self.snapDims(self.CLB_W*0.5)
        lly = y-self.snapDims(self.CLB_H*0.5)
        W1 = self.CLB_W
        H1 = self.CLB_H
        initShape = [(llx, lly, W1, H1)]

        if not self.skipChannels:
            llx += self.CLB_CHAN_L
            lly += self.CLB_CHAN_B
            W1 = self.CLB_W-self.CLB_CHAN_L-self.CLB_CHAN_R
            H1 = self.CLB_H-self.CLB_CHAN_T-self.CLB_CHAN_B
        block_name = f"grid_clb_{xi+1}__{yi+1}_"
        short_block_name = f"LB_{xi+1}_{yi+1}"
        COLOR = self.CLB_COLOR
        points = [0, 0, 0, self.CLB_H, self.CLB_W, self.CLB_H, self.CLB_W, 0]
        self.PlacementDB.append(block_name)
        self.PlacementDBKey[block_name] = {"name": block_name,
                                           "short_name": short_block_name,
                                           "bbox": [llx, lly,
                                                    llx+W1, lly+H1],
                                           "points": points,
                                           "module": "grid_clb_1__1_",
                                           "center": [x, y],
                                           "color": COLOR,
                                           "shape": [(llx, lly, W1, H1)],
                                           "initShape": initShape,
                                           "xi": xi,
                                           "yi": yi}

    def add_cbx(self, xi, yi, lbl=None):
        x, y = (xi+1)*self.CLB_GRID_X, (yi+1)*self.CLB_GRID_Y
        llx = x-self.snapDims((self.CBX_W)*0.5)
        lly = y-self.snapDims((self.CLB_H*0.5)+self.CBX_H)
        W1 = self.CBX_W
        H1 = self.CBX_H
        initShape = [(llx, lly, W1, H1)]

        if not self.skipChannels:
            llx += self.CBX_CHAN_L
            lly += self.CBX_CHAN_B
            W1 = self.CBX_W-self.CBX_CHAN_L-self.CBX_CHAN_R
            H1 = self.CBX_H-self.CBX_CHAN_T-self.CBX_CHAN_B

        block_name = f"cbx_{xi+1}__{yi}_"
        short_block_name = f"CX_{xi+1}_{yi}"
        points = [0, 0, 0, W1, H1, W1, H1, 0]
        self.PlacementDB.append(block_name)
        moduleName = "cbx_1__0_" if yi == 0 else "cbx_1__2_" if yi == self.sizeY else "cbx_1__1_"
        self.PlacementDBKey[block_name] = {"name": block_name,
                                           "short_name": short_block_name,
                                           "bbox": [llx, lly, llx+W1, lly+H1],
                                           "points": points,
                                           "center": [llx+W1*0.5, lly+H1*0.5],
                                           "module": moduleName,
                                           "color": self.CBX_COLOR,
                                           "shape": [(llx, lly, W1, H1)],
                                           "initShape": initShape,
                                           "xi": xi,
                                           "yi": yi}

    def add_cby(self, xi, yi, lbl=None):
        x, y = (xi+1)*self.CLB_GRID_X, (yi+1)*self.CLB_GRID_Y - 1
        llx = x-self.snapDims((self.CLB_W*0.5)+self.CBY_W)
        lly = y-self.snapDims(self.CBY_H)*0.5
        W1 = self.CBY_W
        H1 = self.CBY_H
        initShape = [(llx, lly, W1, H1)]

        if not self.skipChannels:
            llx += self.CBY_CHAN_L
            lly += self.CBY_CHAN_B
            W1 = self.CBY_W-self.CBY_CHAN_L-self.CBY_CHAN_R
            H1 = self.CBY_H-self.CBY_CHAN_T-self.CBY_CHAN_B

        block_name = f"cby_{xi}__{yi+1}_"
        short_block_name = f"CY_{xi}_{yi+1}"
        points = [0, 0, 0, W1, H1, W1, H1, 0]
        self.PlacementDB.append(block_name)
        moduleName = "cby_0__1_" if xi == 0 else "cby_2__1_" if xi == self.sizeY else "cby_1__1_"
        self.PlacementDBKey[block_name] = {"name": block_name,
                                           "short_name": short_block_name,
                                           "bbox": [llx, lly, llx+W1, lly+H1],
                                           "points": points,
                                           "center": [llx+W1*0.5, lly+H1*0.5],
                                           "module": moduleName,
                                           "color": self.CBY_COLOR,
                                           "shape": [(llx, lly, W1, H1)],
                                           "initShape": initShape,
                                           "xi": xi,
                                           "yi": yi}

    def get_stype(self, x, y):
        if x == 0:
            if y == 0:
                return 1
            elif y == self.sizeX:
                return 3
            else:
                return 2
        elif x == self.sizeY:
            if y == 0:
                return 7
            elif y == self.sizeX:
                return 5
            else:
                return 6
        else:
            if y == 0:
                return 8
            elif y == self.sizeX:
                return 4
            else:
                return 0

    def unique(self, sequence):
        seen = set()
        u = [x for x in sequence if not (x in seen or seen.add(x))]
        return [val for sublist in u for val in sublist]

    def add_sb(self, xi, yi):
        '''
                   d
                 +----+
               c |    |
             b   |    |   e
            +----+    +----+
          a |              |           Cross Shape
            |              |           -lengths {a b c d e f}
            +----+    +----+
                 |    |
                 |    | f
                 +----+
        '''
        x = xi*self.CLB_GRID_X - 1
        y = yi*self.CLB_GRID_Y - 1

        llxB1 = x+(self.CLB_W*0.5)
        llyB1 = y+(self.CBY_H*0.5)
        WidthB1 = self.SIDE_X
        HeightB1 = self.SB_H

        llxB2 = x + (self.CBX_W*0.5)
        llyB2 = y + (self.CLB_H*0.5)
        WidthB2 = self.SB_W
        HeightB2 = self.SIDE_Y

        a = self.SIDE_Y
        b = e = (WidthB2-self.SIDE_X)*0.5
        c = f = (HeightB1-self.SIDE_Y)*0.5
        d = self.SIDE_X

        Stype = self.get_stype(xi, yi)
        if Stype == 1:  # SB_0__0_
            llyB1 += c
            HeightB1 += -c
            llxB2 += b
            WidthB2 += -b
            b = f = 0
        elif Stype == 2:  # SB_0__1_
            llxB2 += b
            WidthB2 -= b
            b = 0
        elif Stype == 3:  # SB_0__2_
            llxB2 += b
            WidthB2 -= b
            HeightB1 -= f
            c = b = 0
        elif Stype == 4:  # SB_1__2_
            HeightB1 -= c
            c = 0
        elif Stype == 5:  # SB_2__2_
            HeightB1 -= c
            WidthB2 -= e
            c = e = 0
        elif Stype == 6:  # SB_2__1_
            WidthB2 -= e
            e = 0
        elif Stype == 7:  # SB_2__0_
            llyB1 += f
            HeightB1 -= f
            WidthB2 -= e
            e = f = 0
        elif Stype == 8:  # SB_1__0_
            llyB1 += f
            HeightB1 -= f
            f = 0

        block_name = f"sb_{xi}__{yi}_"
        short_block_name = f"SB_{xi}_{yi}"
        initShape = [(llxB1, llyB1, WidthB1, HeightB1),
                     (llxB2, llyB2, WidthB2, HeightB2)]
        points = self.unique([(b, 0), (b, f),
                              (0, f), (0, (f+a)),
                              (b, (f+a)), (b, (a+c+f)),
                              ((b+d), (a+c+f)), ((b+d), (a+f)),
                              ((b+d+e), (a+f)), ((b+d+e), f),
                              ((b+d), f), ((b+d), 0)])
        self.PlacementDB.append(block_name)
        moduleNames = [
            "sb_1__1_", "sb_0__0_", "sb_0__1_",
            "sb_0__2_", "sb_1__2_", "sb_2__2_",
            "sb_2__1_", "sb_2__0_", "sb_1__0_",
        ]

        llx = min([i[0] for i in initShape])
        lly = min([i[1] for i in initShape])
        self.PlacementDBKey[block_name] = {"name": block_name,
                                           "short_name": short_block_name,
                                           "bbox": [llx, lly, llx+f+a+c, lly+b+d+e],
                                           "points": points,
                                           "center": [llx+(WidthB1*0.5)+b,
                                                      lly+(HeightB2*0.5)+f],
                                           "module": moduleNames[Stype],
                                           "color": self.SB_COLOR,
                                           "shape": initShape,
                                           "xi": xi,
                                           "yi": yi,
                                           "dims": [a, b, c, d, e, f],
                                           "initShape": initShape}

    def moduleFmt(self, mod, X, Y):
        return f"{mod}_{X}__{Y}_"
