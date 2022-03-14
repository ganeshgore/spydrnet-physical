
import math
from copy import deepcopy
from shutil import move
from typing import List

import networkx as nx
import spydrnet as sdn
import svgwrite
from svgwrite.container import Group

DEFAULT_COLOR = " black"


class ConnectPoint:
    ''' This store the individual connections points '''

    def __init__(self, from_x, from_y, to_x, to_y):
        from_x, from_y = int(from_x), int(from_y)
        to_x, to_y = int(to_x), int(to_y)
        assert not ((from_x == to_x) and (from_y == to_y)), \
            "Can not make connection to the same grid"
        assert ((from_x == to_x) and (from_y != to_y)) or \
               ((from_x != to_x) and (from_y == to_y)), \
            "Only horizontal or vertical connections are possible " + \
            f"{from_x}  {from_y} {to_x}  {to_y}"
        self.from_x, self.from_y = (from_x, from_y)
        self.to_x, self.to_y = (to_x, to_y)

        self.from_dir = ""
        self.to_dir = ""
        self._color = DEFAULT_COLOR
        self._update_direction()

    @property
    def distance(self):
        ''' return the connection distance '''
        return abs(self.from_x-self.to_x) + abs(self.from_y-self.to_y)

    @property
    def connection(self):
        ''' return all four connection points '''
        return (self.from_x, self.from_y, self.to_x, self.to_y)

    @property
    def full_connection(self):
        ''' return all four connection points '''
        return (self.from_x, self.from_y, self.to_x, self.to_y, self.from_dir, self.to_dir)

    @property
    def from_connection(self):
        ''' return from connection points '''
        return (self.from_x, self.from_y)

    @property
    def to_connection(self):
        ''' return to connection points '''
        return (self.to_x, self.to_y)

    @property
    def color(self):
        ''' return color of conneton '''
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
        return self._color

    def rotate_connection(self, angle, sizex=None, sizey=None):
        self.from_x, self.from_y = self._rotate_point(
            self.from_connection,
            angle=angle, sizex=sizex, sizey=sizey)
        self.to_x, self.to_y = self._rotate_point(
            self.to_connection,
            angle=angle, sizex=sizex, sizey=sizey)
        self._update_direction()

    def translate_connection(self, x, y):
        self.from_x, self.from_y = self.from_x + x, self.from_y+y
        self.to_x, self.to_y = self.to_x + x, self.to_y+y
        self._update_direction()

    def scale_connection(self, scale, anchor=(0, 0)):
        self.translate_connection(-1*anchor[0], -1*anchor[1])
        self.from_x, self.from_y = self.from_x * scale, self.from_y * scale
        self.to_x, self.to_y = self.to_x * scale, self.to_y * scale
        self.translate_connection(anchor[0], anchor[1])
        self._update_direction()

    def _update_direction(self):
        self.to_dir = self.direction()
        self.from_dir = self.direction(reverse=True)

    def direction(self, reverse=False):
        dx, dy = tuple(x-y for x, y in
                       zip(self.to_connection, self.from_connection))
        if dx == 0 and dy > 0:
            direction = "top"
        elif dx == 0 and dy < 0:
            direction = "bottom"
        elif dx > 0 and dy == 0:
            direction = "right"
        elif dx < 0 and dy == 0:
            direction = "left"
        else:
            direction = None
        if reverse:
            return direction
        else:
            return {"left": "right", "right": "left",
                    "top": "bottom", "bottom": "top"}[direction]

    @staticmethod
    def _rotate_point(point, angle, sizex=None, sizey=None):
        x, y = point
        if angle in (90, ):
            return(sizex-y+1, x)
        elif angle in (180, ):
            return(sizex-x+1, sizey-y+1)
        elif angle in (270, ):
            return(y, sizey-x+1)
        else:
            return point

    def __iter__(self):
        yield from self.connection

    def __str__(self) -> str:
        return "%5d %5d %5d %5d %s" % (self.from_x, self.from_y, self.to_x, self.to_y)

    def __mul__(self, scale):
        return ConnectPoint(scale*self.from_x, scale*self.from_y,
                            scale*self.to_x, scale*self.to_y)

    def __rmul__(self, scale):
        return ConnectPoint(scale*self.from_x, scale*self.from_y,
                            scale*self.to_x, scale*self.to_y)
