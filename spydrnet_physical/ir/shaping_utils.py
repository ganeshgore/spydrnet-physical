
"""
"""
import logging
import typing

import numpy as np

logger = logging.getLogger('spydrnet_logs')

PROP = "VERILOG.InlineConstraints"


class shaping_utils:
    """
    Miscellaneous static methods used while shaping
    """

    @staticmethod
    def PolyArea2D(pts):
        '''
        Find the are of the polygon points
        '''
        pts = list(zip(pts[::2], pts[1::2]))
        lines = np.hstack([pts, np.roll(pts, -1, axis=0)])
        area = 0.5*abs(sum(x1*y2-x2*y1 for x1, y1, x2, y2 in lines))
        return area

    @staticmethod
    def _convert_rect_to_pt(inst):
        """
        Converts rectangular shape placed at specific location to absolute points

        Returns: [(lx, ly), (lx, ly+h), (lx+w, ly+h), (lx+w, ly)]
        """
        loc_x = inst.data[PROP].get("LOC_X", 0)
        loc_y = inst.data[PROP].get("LOC_Y", 0)
        width = inst.reference.data[PROP].get("WIDTH", 0)
        height = inst.reference.data[PROP].get("HEIGHT", 0)
        return [(loc_x, loc_y),
                (loc_x, loc_y+height),
                (loc_x+width, loc_y+height),
                (loc_x+width, loc_y)]

    @staticmethod
    def _convert_cross_to_pt(inst):
        """
        Returns the absolute points of the instance with cross shape
        """
        loc_x = inst.data[PROP].get("LOC_X", 0)
        loc_y = inst.data[PROP].get("LOC_Y", 0)
        a, b, c, d, e, f = inst.reference.data[PROP].get(
            "POINTS", [10, 10, 10, 10, 10, 10])
        return [(loc_x+b, loc_y),
                (loc_x+b, loc_y+f),
                (loc_x, loc_y+f),
                (loc_x, loc_y+f+a),
                (loc_x+b, loc_y+f+a),
                (loc_x+b, loc_y+a+f+c),
                (loc_x+b+d, loc_y+a+f+c),
                (loc_x+b+d, loc_y+a+f),
                (loc_x+b+d+e, loc_y+a+f),
                (loc_x+b+d+e, loc_y+f),
                (loc_x+b+d, loc_y+f),
                (loc_x+b+d, loc_y)]

    @staticmethod
    def _interpret_custom_to_shape(new_instance):
        '''
        Converts custom shapes and points to cross or rectangle
        '''
        shape = new_instance.properties.get("SHAPE", None)
        if not shape == "custom":
            return
        points = new_instance.properties.get("POINTS", None)
        points = points.split()
        if len(points) == 7:
            new_instance.properties["SHAPE"] = "rect"
            new_instance.properties["WIDTH"] = int(points[3])
            new_instance.properties["HEIGHT"] = int(points[4])

    @staticmethod
    def _orientation(origin, p1, p2):
        '''
        '''
        difference = (((p2[0] - origin[0]) * (p1[1] - origin[1]))
                      - ((p1[0] - origin[0]) * (p2[1] - origin[1])))
        return difference

    @staticmethod
    def points_to_path(points):
        """
        Converts the list of outline points to strin representing custom shape

        .. note:: Points should be in the correct order to obtain string

        Args:
            points list((float, float)) : list of x and y points

        """
        sequence_string = ""
        sequence_string += "V" if points[0][0] == points[1][0] else "H"
        sequence_string += " %d %d" % (0, 0)
        pt1 = points[0]
        for pt2 in points[1:]:
            dx = pt2[0] - pt1[0]
            dy = pt2[1] - pt1[1]
            pt1 = pt2
            sequence_string += " %d" % (dx+dy)
        return sequence_string

    @staticmethod
    def get_shapes_outline(array):
        """
        Traces the outline of the given object

        While tracing the outline it enforces rectilinear conenctions

        Args:
            points list((float, float)) : list of x and y points

        """
        points = []
        [points.append(x) for x in array if x not in points]
        _hull_points = []

        start = [pt for pt in points if pt[0]
                 == min([x for x, _ in points])][0]
        point = start
        _hull_points.append(start)

        far_point = None
        while (far_point is not start):

            # get the first point (initial max) to use to compare with others
            p1 = None
            for p in points:
                if not p is point:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
                # Ensure we aren't comparing to self or pivot point
                if not (p2 is point or p2 is p1):
                    direction = shaping_utils._orientation(
                        point, far_point, p2)
                    if direction > 0:
                        far_point = p2
            # Get delta_x and delta_y of current point with previous
            delta_x = far_point[0] - point[0]
            delta_y = far_point[1] - point[1]
            # Check if its not horizontal or vertical connection
            # force it to be horizontal or vertical connetion
            if (delta_x*delta_y):
                delta_x = delta_x/abs(delta_x) if delta_x else 0
                delta_y = delta_y/abs(delta_y) if delta_y else 0
                # Find new intermediate point
                new_pt = \
                    (far_point[0], point[1]) if (delta_x, delta_y) == (-1, 1) else \
                    (far_point[0], point[1]) if (delta_x, delta_y) == (1, -1) else \
                    (point[0], far_point[1]) if (delta_x, delta_y) == (1, 1) else \
                    (point[0], far_point[1]) if (delta_x, delta_y) == (-1, -1) else \
                    (None, None)
                # Add intermediate point and current point
                _hull_points.append(new_pt)
                _hull_points.append(far_point)
            else:
                _hull_points.append(far_point)
            if len(_hull_points) > 2:
                # IF three points in line remove middle point
                pt1, pt, pt2 = _hull_points[-3:]
                if (pt1[0] == pt[0] == pt2[0]) or (pt1[1] == pt[1] == pt2[1]):
                    _hull_points.remove(pt)
            point = far_point
        # check if first point is co linear with second an last point
        pt1, pt, pt2 = _hull_points[-2], _hull_points[0], _hull_points[1]
        if (pt1[0] == pt[0] == pt2[0]) or (pt1[1] == pt[1] == pt2[1]):
            _hull_points.remove(pt)
            _hull_points[-1] = _hull_points[0]
        return "custom", _hull_points

    @staticmethod
    def get_custom_boundary(points):
        '''
        Get boundary points from custom shape
        '''
        path = points.split()
        direction = path[0].lower()
        origin = path[1:3]
        boundary = [int(origin[0]), int(origin[1])]
        for pt in map(int, map(float, path[3:])):
            if direction == 'v':
                # print("v")
                boundary.extend([boundary[-2], boundary[-1]+pt])
                direction = 'h'
            else:
                # print("h")
                boundary.extend([boundary[-2]+pt, boundary[-1]])
                direction = 'v'
            # print(boundary)
        return boundary
