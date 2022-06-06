"""
===============================================
Create memory bank pin placement and connection
===============================================

This example demonstrated how a memeroy bacnk protocol can be inserted in the
pre place and routed module.

The idea here is to optimize the WL and BL pin placement on the tile as well
as restructure the (WL and BL) connectivity with eatch latch. The input this
script is the placment and information of each latch, which can be extracted
from the following tcl script.


.. code-block:: tcl

    foreach_in_collection cell [get_cells *LAT* -hierarchical] {
       echo "[get_attr -name full_name $cell] [get_attr -name origin $cell]"
    } > _filename.txt

**Algorithm**:

- Find total number of configuration elements in the block ``B``
- Find number of WL lines (horizontal lines) ``wl_n = ceil(sqrt(B))``
- Calculate number of BL lines (vertical lines) ``bl_n = B/wl_n``
- Sort each cell with increasing order of ``x_loc``,
  assign bl[0] to first set of ``wl_n`` cells and continue assignement till the end
- Sort each cell with increasing order of ``y_loc``,
  assign wl[0] to first set of ``bl_n`` cells and continue assignement till the end

**Highlight WL connectivity**:

.. image:: ../../../examples/OpenFPGA_config/_memeory_bank_conn_wl_lines.svg
    :width: 80%
    :align: center

**Highlight BL connectivity**:

.. image:: ../../../examples/OpenFPGA_config/_memeory_bank_conn_bl_line.svg
    :width: 80%
    :align: center

**Output tcl**:

.. literalinclude:: ../../../examples/OpenFPGA_config/_eco_changes.tcl
    :language: tcl
    :lines: 1-10

.. literalinclude:: ../../../examples/OpenFPGA_config/_memory_bank_protocol_spydrnet.log
    :language: text

.. note:: This is a linear solution to the problem. A further improvement can be obtained by using a simulated annealing method with the solution received in this example as an initial condition.
"""

import logging
import math

import pandas as pd
import seaborn as sns
import spydrnet as sdn
import svgwrite

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO', filename="memory_bank_protocol")


def main():
    latch_locs = pd.read_csv('latch_placement_dump.txt', sep=" ",
                             names=["cells", "x_loc", "y_loc"])
    # latch_locs = latch_locs.sample(n=10)

    total_mem_elements = latch_locs.shape[0]
    wl_n = math.ceil(math.sqrt(total_mem_elements))
    bl_n = math.ceil(total_mem_elements/wl_n)

    x_min, x_max = int(min(latch_locs["x_loc"])), int(max(latch_locs["x_loc"]))
    y_min, y_max = int(min(latch_locs["y_loc"])), int(max(latch_locs["y_loc"]))

    logger.info("Total mem elements %s", total_mem_elements)
    logger.info("word lines         %s", wl_n)
    logger.info("bit lines          %s", bl_n)
    logger.info("Capacity           %s", wl_n*bl_n)
    logger.info("Extra Conns        %s", (wl_n*bl_n)-total_mem_elements)

    latch_locs = latch_locs.sort_values(by=['x_loc', 'y_loc'])
    x_cuts = latch_locs[::wl_n]['x_loc'].values.tolist() + [x_max]
    bl_lines = [round(sum(pts)*0.5, 2) for pts in zip(x_cuts[:-1], x_cuts[1:])]
    sequence = []
    for i in range(bl_n+1):
        sequence += [f"b{i}"] * (wl_n)
    latch_locs["bl"] = sequence[:latch_locs.shape[0]]

    latch_locs = latch_locs.sort_values(by=['y_loc', 'x_loc'])
    y_cuts = latch_locs[::bl_n]['y_loc'].values.tolist()
    y_cuts += [y_max]
    wl_lines = [round(sum(pts)*0.5, 2) for pts in zip(y_cuts[:-1], y_cuts[1:])]
    latch_locs = latch_locs.sort_values(by=['y_loc', 'x_loc'])
    sequence = []
    for i in range(wl_n+1):
        sequence += [f"w{i}"] * (bl_n)
    latch_locs["wl"] = sequence[:latch_locs.shape[0]]

    logger.info("x_cuts     %s", x_cuts)
    logger.info("y_cuts     %s", y_cuts)
    logger.info("wl_lines   %s", wl_lines)
    logger.info("bl_lines   %s", bl_lines)
    for each in latch_locs["wl"].unique():
        logger.info("wl_line [%s]   %d", each, sum(latch_locs["wl"] == each))
    for each in latch_locs["bl"].unique():
        logger.info("bl_line [%s]   %d", each, sum(latch_locs["bl"] == each))

    render_placement(latch_locs, wl_lines, bl_lines, None, y_cuts,
                     filename="_memeory_bank_conn_wl_lines.svg", highlights="w")
    render_placement(latch_locs, wl_lines, bl_lines, x_cuts, None,
                     filename="_memeory_bank_conn_bl_line.svg", highlights="b")
    write_report(latch_locs)


def write_report(latch_locs):
    with open("_eco_changes.tcl", "w", encoding="UTF-8") as fp:
        wl_n = latch_locs["wl"].unique().size
        fp.write("define_bus -type port -name wl -range {0 %d}\n" % wl_n)
        fp.write("define_bus -type net -name wl -range {0 %d}\n" % wl_n)

        bl_n = latch_locs["bl"].unique().size
        fp.write("define_bus -type port -name wl -range {0 %d}\n" % bl_n)
        fp.write("define_bus -type net -name wl -range {0 %d}\n" % bl_n)

        for _, each in latch_locs.iterrows():
            cell = each['cells']
            fp.write("connect_net -net  bl_in[%s] %s/D\n" %
                     (each['bl'][1:], cell))
            fp.write("connect_net -net  wl_in[%s] %s/G\n" %
                     (each['wl'][1:], cell))


def render_placement(latch_locs, wl_lines, bl_lines,
                     x_cuts=None, y_cuts=None,
                     filename="_sample.svg", highlights="b"):
    dwg = svgwrite.Drawing()
    _, xmax = min(latch_locs["x_loc"]), max(latch_locs["x_loc"])+8
    _, ymax = min(latch_locs["y_loc"]), max(latch_locs["y_loc"])+8
    viewbox = (-4, -4, xmax, ymax)
    dwg.viewbox(*viewbox)
    dwg_main = dwg.add(dwg.g(id="main_frame"))
    dwg.defs.add(dwg.style('''
        #boundary{fill:#FAFAFA; stroke-width:1px; stroke:black}
        .wl_lines{fill:red; stroke-width:0.1px; opacity:0.6;}
        .bl_lines{fill:green; stroke-width:0.1px; opacity:0.6;}
    '''))
    dwg_main.add(dwg.rect(size=(xmax, ymax), insert=(-4, -4), id="boundary"))

    palette = sns.color_palette(None,
                                max(len(wl_lines), len(bl_lines))).as_hex()
    for _, each in latch_locs.iterrows():
        color = {True: 'black'}
        for indx, each_color in enumerate(palette):
            color[each[f"{highlights}l"] == f"{highlights}{indx}"] = each_color
        color = color[True]
        dwg_main.add(dwg.circle(r=0.5, class_="marker", fill=color, stroke="none",
                                center=(each["x_loc"], each["y_loc"])))

    # Add word and bit lines regions
    if x_cuts:
        for indx, pts in enumerate(zip(x_cuts[:-1], x_cuts[1:])):
            min_pt, max_pt = pts
            dwg_main.add(dwg.rect(size=((max_pt-min_pt), ymax), class_="bl_region",
                                  fill=palette[indx],
                                  opacity=0.1, insert=(min_pt, -4)))
    if y_cuts:
        for indx, pts in enumerate(zip(y_cuts[:-1], y_cuts[1:])):
            min_pt, max_pt = pts
            dwg_main.add(dwg.rect(size=(xmax, (max_pt-min_pt)), class_="wl_region",
                                  fill=palette[indx],
                                  opacity=0.1, insert=(-4, min_pt)))

    # Add word and bit lines
    for indx, each_wl in enumerate(wl_lines):
        dwg_main.add(dwg.rect(size=(xmax, 0.05), class_="wl_lines",
                              stroke=palette[indx] if highlights == "w" else 'red',
                              insert=(-4, each_wl)))
    for indx, each_wl in enumerate(bl_lines):
        dwg_main.add(dwg.rect(size=(0.05, ymax), class_="bl_lines",
                              stroke=palette[indx] if highlights == "b" else 'red',
                              insert=(each_wl, -4)))

    dwg.saveas(filename, pretty=True, indent=4)
    return dwg


if __name__ == "__main__":
    main()
