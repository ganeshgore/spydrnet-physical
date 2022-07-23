import logging
import os
import pickle
from copy import deepcopy
from glob import glob
from os import environ
from os.path import basename, dirname, realpath

import spydrnet as sdn
from spydrnet_physical.util import ConnectionPattern, ConnectPointList
from svgwrite.container import Group, Style
from spydrnet_physical.util import FPGAGridGen
from copy import deepcopy


logger = logging.getLogger("spydrnet_logs")

PROJ_NAME = basename(dirname(realpath(__file__)))
LAYOUT = environ.get("LAYOUT", "ultimate")

EXTRA_STYLE = """
text{display:none;}
.marker{display:none;}
"""


def main():
    """
    Architecture render method
    """
    try:
        VPR_ARCH_FILE = glob(("/home/users/saad.khalil/Documents/RS/spydrnet-physical/examples/design_example/FPGA8x4_HETERO/task/arch/vpr_arch.xml"))[0]
        PROJ_NAME = basename(dirname(realpath(__file__)))
    except IndexError:
        logger.exception("Architecture file not found ['task/arch/*vpr*']")
    fpga = FPGAGridGen(
        design_name=PROJ_NAME,
        arch_file=VPR_ARCH_FILE,
        release_root="_release",
        layout=LAYOUT,
    )
    fpga.enumerate_grid()

    WIDTH = (fpga.get_width() * 2) + 3
    HEIGHT = (fpga.get_height() * 2) + 3
    WIDTH_F = (fpga.get_width() * 2) + 3
    HEIGHT_F = (fpga.get_height() * 2) + 3

    level0_pmanager = ConnectionPattern(WIDTH, HEIGHT)
    level0_patt = level0_pmanager.connections
    level1_pmanager = ConnectionPattern(WIDTH, HEIGHT)
    level1_patt = level1_pmanager.connections
    level2_pmanager = ConnectionPattern(WIDTH, HEIGHT)
    level2_patt = level2_pmanager.connections
    level3_pmanager = ConnectionPattern(WIDTH, HEIGHT)
    level3_patt = level3_pmanager.connections

    p_manager = ConnectionPattern(WIDTH, HEIGHT)
    hyb_pat = p_manager.connections

    level0_patt.cursor = ((WIDTH / 2)+1, 0)
    level0_patt.move_y(steps=HEIGHT - 2)
    level0_patt.merge(
        p_manager.get_htree(WIDTH, root=2, side=-9).translate(
            0, -(fpga.get_height())
        )
    )
    level0_patt.set_color("green")
    # level0_patt.pull_connection_up(level3_patt.points[0])

    for x in [int(WIDTH / 4) - 1, WIDTH - 16]:
        for y in [10, HEIGHT - 10]:
            if y == HEIGHT - 10 and x == int(WIDTH / 4) - 1:
                level1_patt.merge(
                    p_manager.get_htree(int(WIDTH / 2), root = -1, side=-4).translate(
                        x - 17, y - 16
                    )
                )
            if y == 10 and x == int(WIDTH / 4) - 1:
                level1_patt.merge(
                    p_manager.get_htree(int(WIDTH / 2), root = -1,side=-4).translate(
                        x - 17, y - 17
                    )
                )
            if y == HEIGHT - 10 and x == WIDTH - 16:
                level1_patt.merge(
                    p_manager.get_htree(int(WIDTH / 2), root = -1, side=-4).translate(
                        x - 15, y - 16
                    )
                )
            if y == 10 and x == WIDTH - 16:
                level1_patt.merge(
                    p_manager.get_htree(int(WIDTH / 2), root = -1, side=-4).translate(
                        x - 15, y - 17
                    )
                )

    for x in [7, 23, 43, 59]:
        for y in [6, 14, 22, 30]:
            if x == 7:
                level2_patt.merge(
                    level2_pmanager.get_htree(int(WIDTH / 4)-1, side=-2).translate(
                        x-7 , y-8 
                    )
                )
            if x == 23:
                level2_patt.merge(
                    level2_pmanager.get_htree(int(WIDTH / 4)-1, side=-2).translate(
                        x-9 , y-8 
                    )
                )
            if x == 43:
                level2_patt.merge(
                    level2_pmanager.get_htree(int(WIDTH / 4)-1, side=-2).translate(
                        x-5 , y-8 
                    )
                )
            if x == 59:
                level2_patt.merge(
                    level2_pmanager.get_htree(int(WIDTH / 4)-1, side=-2).translate(
                        x-7 , y-8 
                    )
                )

    for x in [3, 11, 19, 27, 39, 47, 55, 63]:
        for y in range(4, HEIGHT, 4):
            if x == 3 or x == 11:
                level3_patt.merge(
                    level3_pmanager.get_htree(int(WIDTH / 12)).translate(x - 2, y - 3)
                )

            if x == 19 or x == 27:
                level3_patt.merge(
                    level3_pmanager.get_htree(int(WIDTH / 12)).translate(x - 4, y - 3)
                )

            if x == 39 or x == 47:
                level3_patt.merge(
                    level3_pmanager.get_htree(int(WIDTH / 12)).translate(x , y - 3)
                )

            if x == 55 or x == 63:
                level3_patt.merge(
                    level3_pmanager.get_htree(int(WIDTH / 12)).translate(x - 2, y - 3)
                )


# what is more preferable 
#   1 pattern with all the connection    or
#   multiple patterns with small connections

    pts1 = ConnectPointList(30, 3)
    pts1.cursor = (1, 2)
    pts1.hold_cursor()
    pts1.move_x(2)
    pts1.cursor = (7, 3)
    pts1.hold_cursor()
    pts1.move_x(-2).move_cursor_y(-2)
    pts1.move_x(-2)
    pts1.cursor = (9, 2)
    pts1.hold_cursor()
    pts1.move_x(2)
    pts1.cursor = (15, 3)
    pts1.hold_cursor()
    pts1.move_x(2).move_cursor_y(-2)
    pts1.move_x(2)
    pts1.cursor = (21, 2)
    pts1.hold_cursor()
    pts1.move_x(-2)
    pts1.cursor = (23, 3)
    pts1.hold_cursor()
    pts1.move_x(2).move_cursor_y(-2)
    pts1.move_x(2).move_cursor_y(1)
    pts1.move_x(4)
    pts1.cursor = (30, 3)
    pts1.hold_cursor()
    pts1.move_x(-1).move_cursor_y(-2)
    pts1.move_x(-1)
    pts1.set_color("red")
    for x in [4]:
        for y in range(2, HEIGHT - 1, 4):
            pts1_copy = deepcopy(pts1)
            level3_patt.merge(pts1_copy.translate(x, y))

    for x in [WIDTH-3]:
        for y in range(2, HEIGHT - 1, 4):
            pts2_copy = deepcopy(pts1)
            pts2_copy.flip('h')
            level3_patt.merge(pts2_copy.translate(x, y))       


    #pts2 = ConnectPointList(3, 3)
    #pts2.cursor = (1, 1)
    #pts2.hold_cursor()
    #pts2.move_x(2).move_cursor_y(-2)
    #pts2.move_x(2)
    #pts2.set_color("red")
#
    #for x in [20, 28, 58]:
    #    for y in range(2, HEIGHT - 1, 4):
    #        pts1_copy = deepcopy(pts1)
    #        level3_patt.merge(pts1_copy.translate(x, y))
#
    #pts0 = ConnectPointList(3,1)
    #pts0.cursor = (2,1)
    #pts0.hold_cursor()
    #pts0.move_x(1)
    #pts0.move_x(-1)
#
    #for y in range(2, HEIGHT - 1, 2):
    #        pts0_copy = deepcopy(pts0)
    #        level0_patt.merge(pts0_copy.translate(int(WIDTH/2)-1, y))
#
    #pts3 = ConnectPointList(21,1)
    #pts3.cursor = (1,1)
    #pts3.hold_cursor()
    #pts3.move_x(2)
    #pts3.cursor = (13,1)
    #pts3.hold_cursor()
    #pts3.move_x(-2)
    #pts3.cursor = (21,1)
    #pts3.hold_cursor()
    #pts3.move_x(-2)
    #
    #for x in [4, int(WIDTH/2)+9]:
    #    for y in range(3, HEIGHT - 1, 4):
    #        pts3_copy = deepcopy(pts3)
    #        level3_patt.merge(pts3_copy.translate(x, y)) 
#
    ##pts4 = ConnectPointList(3,1)
    ##pts4.cursor = (3,1)
    ##pts4.hold_cursor()
    ##pts4.move_x(-2)
##
    ##for x in [int(WIDTH/2)-11, WIDTH-7]:
    ##    for y in range(3, HEIGHT - 1, 4):
    ##        pts4_copy = deepcopy(pts4)
    ##        level3_patt.merge(pts4_copy.translate(x, y)) 
    #
    #pts5 = ConnectPointList(15,1)
    #pts5.cursor = (1,1)
    #pts5.hold_cursor()
    #pts5.move_x(4)
    #pts5.cursor = (15, 1)
    #pts5.hold_cursor()
    #pts5.move_x(-4)
#
    #for x in [int(WIDTH/2)-7]:
    #    for y in range(3, HEIGHT - 1, 4):
    #        pts5_copy = deepcopy(pts5)
    #        level3_patt.merge(pts5_copy.translate(x, y)) 

    remove_points = []
    for x in [15, int(WIDTH/2)+20]:
        for y in range(12, HEIGHT-8, 4):
            remove_points.append((x, y))
            for point in remove_points:
                point = level3_patt.search_to_point(point)
                if point:
                    level3_patt._points.remove(point)

    # TODO Not working... need to short points on both the DSP columns.
    short_points = []
    for x in [16]:
        for y in range(17, HEIGHT-8, 2):
            short_points.append((x, y))
            for point in short_points:
                to_point = level3_patt.search_to_point(point)
                from_point = level3_patt.search_from_point(point)
                if to_point and from_point:
                    level3_patt.short_through(point)

    hyb_pat.merge(level0_patt)
    hyb_pat.merge(level1_patt)
    hyb_pat.merge(level2_patt)
    hyb_pat.merge(level3_patt)

    scale = 7
    svg = p_manager.render_pattern(title=PROJ_NAME, scale=scale)

    hetro_columns = [3, 7]
    if LAYOUT == "ultimate":
        hetro_columns += [11, 15, 18, 22, 26, 30]
    skip_points = [(1, 1), (1, HEIGHT), (WIDTH, 1), (WIDTH, HEIGHT)]
    skip_points += [(x * 2, y) for x in hetro_columns for y in range(5, HEIGHT, 4)]

    extra_pts = []
    # extra_pts += [(x * 2, y - 1) for x in hetro_columns for y in range(5, HEIGHT, 4)]
    # extra_pts += [(x * 2, y) for x in hetro_columns for y in range(5, HEIGHT, 4)]

    sink_pts = p_manager.svg_main.add(Group(id="sink_pts"))
    for y in list(range(3, HEIGHT, 2)) + [1, HEIGHT]:
        for x in list(range(3, WIDTH, 2)) + [1, WIDTH]:
            if not (x, y) in skip_points:
                sink_pts.add(
                    svg.rect(
                        insert=(
                            (x * scale) - (0.5 * scale),
                            (y * scale) - (0.5 * scale),
                        ),
                        size=(scale, scale),
                        opacity=0.2,
                        class_="sink_point",
                    )
                )
    for x, y in extra_pts:
        sink_pts.add(
            svg.rect(
                insert=(x * 20 - 10, y * 20 - 10),
                size=(20, 20),
                opacity=0.2,
                fill="red",
                class_="sink_point",
            )
        )

    svg.saveas(f"{PROJ_NAME}_{LAYOUT}_clock0_clear_tree.svg", pretty=True, indent=4)
    save_svg_with_background(svg, f"{PROJ_NAME}_{LAYOUT}_clock0_tree.svg")


# FIXME: This needs some more planning to implment, coupple of problem are
# 1. Render for grid
# 2. Color schemeto match
# I belive we should add some styling functions to the FPGA grid gen


def save_svg_with_background(svg, filename, add_marker=False):
    fpga = pickle.load(open(f"{PROJ_NAME}_{LAYOUT}_fpgagridgen.pickle", "rb"))
    scalex, scaley = 1, 1

    # Add main group
    groups = {ele["id"]: ele for ele in svg.elements if isinstance(ele, Group)}
    main_group = groups["main"]

    for style in [ele for ele in svg.elements if isinstance(ele, Style)]:
        fpga.dwg.defs.add(style)
    fpga.dwg.defs.add(fpga.dwg.style(EXTRA_STYLE))

    connections_dwg = fpga.dwg.add(
        Group(id="connection", transform=f"scale({scalex},-{scaley}) translate(-2, -2)")
    )

    for ele in main_group.elements:
        connections_dwg.add(ele)
    fpga.dwg.saveas(filename, pretty=True, indent=4)


if __name__ == "__main__":
    main()
