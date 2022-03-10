"""
This file contains OpenFPGA Architecture parser class
It is desigend to provide a API interface to probe architecrure related data
"""

import xml.etree.ElementTree as ET
from spydrnet_physical.util.shell import launch_shell


class OpenFPGA_Arch:

    def __init__(self, vpr_arch, openfpga_arch) -> None:
        self.vpr_arch = ET.parse(vpr_arch).getroot()
        self.openfpga_arch = ET.parse(openfpga_arch).getroot()
        self._pb_types = self._get_pb_types()

    @property
    def pb_types(self):
        return self._pb_types

    def _get_pb_types(self):
        return [pb.get('name') for pb in self.vpr_arch.findall("./complexblocklist/pb_type")]

    def get_layouts(self):
        '''
        Returns available layouts in the architecture
        '''
        layout = {}
        for each in self.vpr_arch.find("layout").findall("fixed_layout"):
            layout[each.get("name")] = (int(each.get("width")),
                                        int(each.get("height")))
        return layout

    def is_homogeneous(self):
        """
        Checks if the device is homogeneous device or heterogenous
        """
        layout = self.vpr_arch.find("layout").findall("fixed_layout")[0]
        print(layout.findall("clb"))
