
'''
This file creates different connection patterns for connectivity

The connection pattern format
# FROM_X, FROM_Y, TO_X, TO_Y


for external connections (its 45 degree clock wise ratation)
0, 0 : Left
None, 0 : bottom
None, None : Right
0, None : Top
'''
import math
from copy import deepcopy
from shutil import move
from typing import List

import networkx as nx
import spydrnet as sdn
import svgwrite
from spydrnet_physical.util import (ConnectPoint, ConnectPointList)
from svgwrite.container import Group

DEFAULT_COLOR = " black"


class ConnectionPattern:
    '''
    This creates a connection patterns (`ConnectPointList`) based on pre-defined rule

    '''

    def __init__(self, sizex, sizey):
        '''
        Initialise FPGA parameters

        args:
            sizex (int): Width of FPGA grid
            sizey (int): Size of FPGA grid
        '''
        self.sizex = sizex
        self.sizey = sizey
        self.xbias = 0
        self.ybias = 0
        self.dwg_main = None
        self._connect = ConnectPointList(sizex=sizex, sizey=sizey)

    @property
    def svg_main(self):
        return self.dwg_main

    @ property
    def connections(self):
        return self._connect

    @ connections.setter
    def connections(self, value):
        self._connect = value
        return self._connect

    def reset(self):
        self._connect = ConnectPointList(sizex=self.sizex,
                                         sizey=self.sizey)

    @ staticmethod
    def _get_prime_factors(number):
        prime_factors = []
        while number % 2 == 0:
            prime_factors.append(2)
            number = number / 2

        for i in range(3, int(math.sqrt(number)) + 1, 2):
            while number % i == 0:
                prime_factors.append(int(i))
                number = number / i
        if number > 2:
            prime_factors.append(int(number))
        return prime_factors

    def auto_select(self):
        '''
        Auto implements the global tree with crop and scale operations
        '''
        NotImplementedError

    @staticmethod
    def get_htree(size, root=0, side=0, repeat=1):
        ''' Returns H-Tree of specific size '''
        points = ConnectPointList(sizex=size, sizey=size)
        size = size if size % 2 else (size-1)
        mid = (size+1)/2
        points.cursor = (mid, mid)
        for _ in range(repeat):
            points.release_cursor()
            points.move_x(value=1, steps=int(mid/2)+root)
            points.hold_cursor()
            points.move_y(value=1, steps=int(mid/2)+side)
            points.move_y(value=-1, steps=int(mid/2)+side)

        points.cursor = (mid, mid)
        for _ in range(repeat):
            points.release_cursor()
            points.move_x(value=-1, steps=int(mid/2)+root)
            points.hold_cursor()
            points.move_y(value=1, steps=int(mid/2)+side)
            points.move_y(value=-1, steps=int(mid/2)+side)
        return points

    def add_htree(self, n=3):
        '''
        Returns HTree pattern fo the given grid size
        '''
        assert (math.log2(n-1) % 1) == 0, "Support only (2^n)+1 width"
        self._connect.merge(self.get_htree(n))
        return self._connect

        dev_size = min(self.sizex, self.sizey)
        while n < dev_size:
            print(n)
            n = n*2
            self.get_fishbone()
        return self._connect
        # points = self._connect
        # x_center = ((self.sizex+1)*0.5)
        # y_center = ((self.sizey+1)*0.5)
        # print(x_center, y_center)

    def get_fishbone(self, width=None, height=None, steps=1, x_margin=(0, 0), y_margin=(0, 0)):
        '''
        Returns fishbone pattern for the given grid size

        Spine is created at the center of the grid, to change bias when grid
        is symetric change ``xbias`` and ``ybias`` parameter

        x_margin(tuple(int, int)): Skips the repective grid connectivity
        y_margin(tuple(int, int)): Skips the repective grid connectivity
        '''
        width = width or self.sizex
        height = height or self.sizey
        points = self._connect
        x_center = ((width+1)*0.5)
        x_pt = math.ceil(x_center) if self.xbias else math.floor(x_center)
        y_pt = (1+y_margin[0])
        points.add_connection(x_pt, 0, x_pt, y_pt)
        points.cursor = (x_pt, y_pt)
        for indx in range(0, height-y_margin[1], steps):
            if not indx == 0:
                points.move_y(steps=steps)
            center = points.cursor
            while points.get_x < (width-x_margin[1]):
                points.move_x()
            points.cursor = center
            while points.get_x > (1 + x_margin[0]):
                points.move_x(-1)
            points.cursor = center
        return points

    def render_pattern(self, scale=20, title=None, add_module_labels=False):
        dwg = self._connect.render_pattern(scale)

        self.dwg_main = [e for e in dwg.elements if e.get_id() == "main"][0]
        dwgText = self.dwg_main.add(Group(id="text"))
        dwgMarker = [e for e in dwg.elements if e.get_id() == "markers"]

        if dwgMarker:
            dwgMarker = dwgMarker[0]
            for i in range(0, self.sizex+1):
                dwgMarker.add(dwg.line(start=((i+0.5)*scale, 0.5*scale),
                                       end=((i+0.5)*scale,
                                            (self.sizey+0.5)*scale),
                                       class_="gridmarker"))
            for i in range(0, self.sizey+1):
                dwgMarker.add(dwg.line(start=(0.5*scale, (i+0.5)*scale),
                                       end=((self.sizex+0.5) *
                                            scale, (i+0.5)*scale),
                                       class_="gridmarker"))

        # Add labels to the grid
        if add_module_labels:
            for x in range(1, 1+self.sizex):
                for y in range(1, 1+self.sizey):
                    txt = self._connect.get_top_instance(x, y).name
                    label = dwg.text("",
                                     font_size=self.sizey*scale*0.03,
                                     alignment_baseline="middle",
                                     class_="gridLabels",
                                     text_anchor="middle",
                                     transform="scale(1,-1)",
                                     insert=(x*scale, (-1*y*scale) + 0.25*scale))
                    label.add(dwg.tspan(txt, x=[x*scale]))
                    label.add(dwg.tspan(
                        "["+self._connect.get_reference(x, y)+"]",
                        font_size=self.sizey*scale*0.02,
                        x=[x*scale], dy=["2%", ]))
                    dwgText.add(label)

        # Add title to generated SVG image
        title = title or f" %d x %d FPGA " % (self.sizex, self.sizey)
        dwgText.add(dwg.text(title,
                             insert=((self.sizex+1)*scale*0.5, -1*-0.5*scale),
                             transform="scale(1,-1)",
                             class_="moduleLabel",
                             fill="black",
                             font_size=self.sizey*scale*0.1,
                             alignment_baseline="middle",
                             text_anchor="middle"))

        width = self.sizex*scale + (scale)
        height = self.sizey*scale + (3*scale)
        x_offset = 0
        y_offset = -1*height + (1.5*scale)
        dwg["width"] = width
        dwg["height"] = height
        dwg.viewbox(x_offset, y_offset, width, height)

        return dwg


if __name__ == "__main__":
    # conn_list = ConnectPointList(5, 5)
    # conn_list.add_connection(1, 1, 1, 2)
    # conn_list.add_connection(1, 2, 2, 2)
    # print(conn_list)
    # conn_list.render_pattern().save(pretty=True, indent=4)

    # fpga = ConnectionPattern(5, 5)
    # conn_list = fpga.get_fishbone()
    # print(conn_list)
    # conn_list.rotate(90)
    # fpga.render_pattern().save(pretty=True, indent=4)

    fpga = ConnectionPattern(5, 5)
    left_tree = fpga.connections
    left_tree = fpga.get_fishbone(x_margin=(0, 0))
    left_tree.scale(2, anchor=(1, 1))

    fpga = ConnectionPattern(10, 10)
    conn_list = fpga.connections
    conn_list.merge(left_tree)
    conn_list.crop_edges()
    conn_list.sample_connections()
    fpga.render_pattern().save(pretty=True, indent=4)
