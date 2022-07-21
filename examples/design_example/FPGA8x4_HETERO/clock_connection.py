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
        VPR_ARCH_FILE = glob(("task/arch/*vpr*"))[0]
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

    level0_patt.cursor = (WIDTH / 2, 0)
    level0_patt.move_y(steps=int(HEIGHT / 2) + 1)
    level0_patt.merge(
        p_manager.get_htree(WIDTH, root=2, side=-8).translate(
            0, -(fpga.get_height() - 1)
        )
    )
    level0_patt.set_color("green")
    # level0_patt.pull_connection_up(level3_patt.points[0])

    for x in [int(WIDTH / 4) - 1, WIDTH - 16]:
        for y in [10, HEIGHT - 10]:
            if y == HEIGHT - 10 and x == int(WIDTH / 4) - 1:
                level1_patt.merge(
                    p_manager.get_htree(int(WIDTH / 2), side=-4).translate(
                        x - 17, y - 16
                    )
                )
            if y == 10 and x == int(WIDTH / 4) - 1:
                level1_patt.merge(
                    p_manager.get_htree(int(WIDTH / 2), side=-4).translate(
                        x - 17, y - 17
                    )
                )
            if y == HEIGHT - 10 and x == WIDTH - 16:
                level1_patt.merge(
                    p_manager.get_htree(int(WIDTH / 2), side=-4).translate(
                        x - 16, y - 16
                    )
                )
            if y == 10 and x == WIDTH - 16:
                level1_patt.merge(
                    p_manager.get_htree(int(WIDTH / 2), side=-4).translate(
                        x - 16, y - 17
                    )
                )

    for x in [7, 23, 43, 59]:
        for y in [6, 14, 22, 30]:
            level2_patt.merge(
                level2_pmanager.get_htree(int(WIDTH / 4), side=-2).translate(
                    x - 8, y - 8
                )
            )

    for x in [3, 11, 19, 27, 39, 47, 55, 63]:
        for y in range(4, HEIGHT, 4):
            level3_patt.merge(
                level3_pmanager.get_htree(int(WIDTH / 12)).translate(x - 3, y - 3)
            )

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
