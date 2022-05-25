from collections import namedtuple
import matplotlib.pyplot as plt
import random


def _get_orientation(origin, p1, p2):
    difference = (
        ((p2[0] - origin[0]) * (p1[1] - origin[1]))
        - ((p1[0] - origin[0]) * (p2[1] - origin[1])))
    return difference


def compute_hull(points):
    '''
    Computes the points that make up the convex hull.
    :return:
    '''
    _hull_points = []

    start = [pt for pt in points if pt[0] == min([x for x, _ in points])][0]
    point = start
    _hull_points.append(start)

    far_point = None
    while far_point is not start:

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
                direction = _get_orientation(point, far_point, p2)
                if direction > 0:
                    far_point = p2
        _hull_points.append(far_point)
        point = far_point
    return _hull_points


def display(_points, _hull_points):
    # all points
    x = [p[0] for p in _points]
    y = [p[1] for p in _points]
    plt.plot(x, y, marker='D', linestyle='None')

    # hull points
    hx = [p[0] for p in _hull_points]
    hy = [p[1] for p in _hull_points]
    plt.plot(hx, hy, 'ro--')

    plt.title('Convex Hull')
    plt.savefig("_convex_hull_solution.png")


def main():
    points = []
    for _ in range(35):
        points.append((random.randint(0, 10), random.randint(0, 10)))

    points = [(90, 210), (130, 170), (50, 170), (170, 170), (50, 250),
              (90, 170), (90, 250), (130, 210), (50, 210), (170, 210)]
    hull_points = compute_hull(points)
    cross_conn = [(pt1, pt2)
                  for pt1, pt2 in zip(hull_points[:-1], hull_points[1:])
                  if (abs(pt1[0]-pt2[0])*abs(pt1[1]-pt2[1]))]
    for each_pt_pair in cross_conn[:]:
        pt1, pt2 = each_pt_pair
        dx = 1 if pt2[0] > pt1[0] else -1
        dy = 1 if pt2[1] > pt1[1] else -1
        new_point = (pt2[0], pt1[1]) if (dx, dy) == (-1, 1) else \
                    (pt2[0], pt1[1]) if (dx, dy) == (1, -1) else \
                    (pt1[0], pt2[1]) if (dx, dy) == (1, 1) else \
                    (pt1[0], pt2[1]) if (dx, dy) == (-1, -1) else \
                    (None, None)
        index = hull_points.index(pt1)
        hull_points.insert(index+1, new_point)

    indx = 1
    while indx < len(hull_points)-1:
        pt1 = hull_points[indx-1]
        pt = hull_points[indx]
        pt2 = hull_points[indx+1]
        if (pt1[0] == pt[0] == pt2[0]) or (pt1[1] == pt[1] == pt2[1]):
            hull_points.remove(pt)
        indx += 1

    sequence_string = ""
    sequence_string += "H" if hull_points[0][0] == hull_points[1][0] else "V"
    sequence_string += " %d %d" % hull_points[0]
    pt1 = hull_points[0]
    for pt2 in hull_points[1:-1]:
        dx = pt2[0] - pt1[0]
        dy = pt2[1] - pt1[1]
        sequence_string += " %d" % (dx+dy)
    print(sequence_string)
    display(points, hull_points)


if __name__ == '__main__':
    main()
