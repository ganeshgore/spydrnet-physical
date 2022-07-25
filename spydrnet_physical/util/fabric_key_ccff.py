'''
'''
import logging
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

import spydrnet as sdn
import svgwrite
from spydrnet_physical.util import FPGAGridGen

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


class FabricKeyGenCCFF:
    ''' This stores list of connection points  '''
    fkey: list = [[]]

    def __init__(self, fpga_grid=None, design_name=None,
                 arch_file=None, layout=None):

        if not fpga_grid:
            self.design_name = design_name
            self.arch_file = arch_file
            self.layout = layout
            fpga_grid = FPGAGridGen(design_name="", arch_file=arch_file,
                                    release_root="", layout=layout)
            fpga_grid.enumerate_grid()
            fpga_grid.render_layout()

        self.fpga_grid = fpga_grid
        self.dwg = fpga_grid.dwg
        self.dwg_shapes = fpga_grid.dwg_shapes
        self.dwg_text = fpga_grid.dwg_text

    def save_fabric_key(self, filename):
        '''
        Saves the fabric key as XML

        Args:
            filename (str): Fabric key filename
        '''
        start = 0
        key = ET.Element('fabric_key')
        for index, region_elements in enumerate(self.fkey):
            region = ET.SubElement(key, "region", {'id': str(index)})
            for each in region_elements:
                inst_name = each[-1]
                if (each[0] % 2 == 0) and (each[1] % 2 == 0):
                    inst_name = "grid_" + inst_name
                ET.SubElement(region, 'key', {'id': str(start),
                                              'alias': inst_name})
                start += 1
        with open(filename, "w", encoding="UTF-8") as fptr:
            rough_string = ET.tostring(key, 'utf-8')
            reparsed = minidom.parseString(rough_string)
            fptr.write(reparsed.toprettyxml(indent="  "))

    @staticmethod
    def instance_to_coordinate(self, instance_name,
                               regex=r".*_([0-9]+)__([0-9]+)_"):
        match = re.match(regex, instance_name)
        return match.group(1), match.group(2)

    def create_serpentine_connection(self):
        for xpt in range(0, (self.fpga_grid.get_width()*2)+3, 2):
            for ypt in range((self.fpga_grid.get_height()*2)+3):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                self.fkey[0] += [(xpt, ypt, inst_name)]
            for ypt in range((self.fpga_grid.get_height()*2)+3)[::-1]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt+1, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                self.fkey[0] += [(xpt+1, ypt, inst_name)]

    def create_sel_serpentine_connection(self, x, fkey_name):
        for xpt in [x]:
            for ypt in range((self.fpga_grid.get_height()*2)+3):
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    fkey_name += [(xpt, ypt, inst_name)]  
            for ypt in range((self.fpga_grid.get_height()*2)+3)[::-1]:
                    try:
                        inst_name = self.fpga_grid.get_top_instance(xpt+1, ypt)
                    except IndexError:
                        break
                    if inst_name == "EMPTY":
                        continue
                    fkey_name += [(xpt+1, ypt, inst_name)]
            
    
    def create_bot2top_connection(self, x, y1, y2, fkey_name):
        for xpt in [x]:
            for ypt in range(y1, y2+1, 1):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey_name += [(xpt, ypt, inst_name)]

    def create_top2bot_connection(self, x, y1, y2, fkey_name): 
        for xpt in [x]:
            for ypt in range(y1, y2-1, -1):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey_name += [(xpt, ypt, inst_name)]
    
    def create_left2right_connection(self, x1, x2, y, fkey_name):
        for ypt in [y]:    
            for xpt in range(x1, x2+1, 1):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey_name += [(xpt, ypt, inst_name)]

    def create_right2left_connection(self, x1, x2, y, fkey_name):
        for ypt in [y]:    
            for xpt in range(x1, x2-1, -1):
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                fkey_name += [(xpt, ypt, inst_name)]
                
    def create_diagonal_connection(self, x1, x2, y1, y2, fkey_name):

        for ypt in [y1, y2]:    
            for xpt in [x1, x2]:
                try:
                    inst_name = self.fpga_grid.get_top_instance(xpt, ypt)
                except IndexError:
                    break
                if inst_name == "EMPTY":
                    continue
                if (x1 and y1) or (x2 and y2):
                    fkey_name += [(xpt, ypt, inst_name)]

    def create_fabric_key(self, pattern=None):
        '''
        Main fucntion to create fabric key

        Args:
            pattern (str): Type of fabric key pattern
        '''
        if pattern == "serpentine":
            self.create_serpentine_connection()
        else:
            self.create_serpentine_connection()
        return self.fkey

    def render_svg(self, filename, skip_instance="grid_io*"):
        '''
        This method renders the fabric key on the given FPGA grid

        Args:
            design_name (str): Design name
            filename (str): name of the SVG file to store
            show_grid_io (str): name of the SVG file to store
            skip_instance (str): Regex match string to skip instances
        '''
        dwg = self.dwg

        marker = dwg.marker(refX="30", refY="30",
                            viewBox="0 0 120 120",
                            markerUnits="strokeWidth",
                            markerWidth="8", markerHeight="10", orient="auto")
        marker.add(dwg.path(d="M 0 0 L 60 30 L 0 60 z", fill="blue"))
        dwg.defs.add(marker)

        mapping = {}
        for element in self.dwg_text.elements:
            mapping[element.text] = (float(element.attribs["x"]),
                                     -1*float(element.attribs["y"]))

        for each_region in self.fkey:
            points = []
            for each_instance in each_region:
                points += map(str, mapping[each_instance[-1]])
            self.dwg_shapes.add(dwg.path(d=f"M {points[0]} {points[1]} " +
                                         " ".join(points), fill="none",
                                         marker_mid=marker.get_funciri(),
                                         marker_end=marker.get_funciri(),
                                         stroke_width='0.4px', stroke="red"))

        if filename:
            self.dwg.saveas(filename, pretty=True, indent=4)
            print(f"SVG file saved as {filename}")
        return self.dwg
