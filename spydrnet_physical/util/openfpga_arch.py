"""
This file contains OpenFPGA Architecture parser class
It is desigend to provide a API interface to probe architecrure related data
"""

from xml.dom.minidom import Element
import xml.etree.ElementTree as ET
from spydrnet_physical.util.shell import launch_shell


class OpenFPGA_Arch:

    def __init__(self, vpr_arch, openfpga_arch, layout) -> None:
        self.vpr_arch = vpr_arch if isinstance(
            vpr_arch, ET.Element) else ET.parse(vpr_arch).getroot()
        if openfpga_arch:
            self.openfpga_arch = openfpga_arch if isinstance(
                openfpga_arch, ET.Element) else ET.parse(openfpga_arch).getroot()
        self._pb_types = self._get_pb_types()
        self._tiles = self._get_tiles()
        self._tiles.update({"EMPTY": (1, 1)})
        self.set_layout(layout)
        self.grid = [[0 for x in range(self.width)]
                     for y in range(self.height)]

    def get_width(self):
        ''' Get width of FPGA '''
        return self.width-2

    def get_height(self):
        ''' Get height of FPGA '''
        return self.height-2

    @property
    def pb_types(self):
        return self._pb_types

    @property
    def tiles(self):
        return self._tiles

    @property
    def layout(self):
        return self._layout

    def _get_pb_types(self):
        return {pb.get('name'): (int(pb.get('width', 1)), int(pb.get('height', 1)))
                for pb in self.vpr_arch.findall("./complexblocklist/pb_type")}

    def _get_tiles(self):
        return {tile.get('name'): (int(tile.get('width', 1)), int(tile.get('height', 1)))
                for tile in self.vpr_arch.findall("./tiles/tile")}

    def get_layouts(self):
        '''
        Returns available layouts in the architecture
        '''
        layout = {}
        for each in self.vpr_arch.find("layout").findall("fixed_layout"):
            layout[each.get("name")] = (int(each.get("width")),
                                        int(each.get("height")))
        return layout

    def set_layout(self, layout_name):
        """ Set speific layout as primary layout """
        layouts = self.get_layouts().keys()
        assert layout_name in self.get_layouts().keys(), \
            "%s layout not found, [%s]" % (layout_name, ", ".join(layouts))
        self._layout = self.vpr_arch.find("layout").find(
            f"fixed_layout[@name='{layout_name}']")
        self.width = int(self._layout.attrib.get("width", 1))
        self.height = int(self._layout.attrib.get("height", 1))

    def is_homogeneous(self):
        """
        Checks if the device is homogeneous device or heterogenous

        if layout section contains anything other than `corner`, `periphery` and 
        `fill` the device is consider as a homogeneous 
        """
        layout = self.vpr_arch.find("layout").findall("fixed_layout")[0]
        print(layout.findall("clb"))
