"""
=========================
Splitting Connection box
=========================

This example demonstrate, how connection box can be split into two parts 
to be merged with the respective logic blocks.

It first converts the pre tech-mapped connection box netlist to a 
networkX graph. The graph is converted to a two dimentional array and 
passed to metis library which performs the partitioning.
The partitioned graph is rendered in the following SVG. 

To simplify the partitioning, all the global signals are stripped down 
before converting netlist to a graph (including connections beetween 
shift registers chain).

.. image:: ../../../examples/OpenFPGA/_graph.svg
    :width: 500px
    :align: center

"""

import glob
import logging
import os
import tempfile
from itertools import chain
from pprint import pprint
import networkx as nx
from fnmatch import fnmatch
import numpy as np

import pymetis
import pydot
import spydrnet as sdn
from networkx.drawing.nx_agraph import write_dot
from networkx.drawing.nx_pydot import to_pydot
from spydrnet_physical.util import OpenFPGA, config_chain_simple, get_names
from spydrnet_physical.util.get_floorplan import FloorPlanViz
from spydrnet_physical.util.shell import launch_shell
from spydrnet_physical.util import write_metis_graph, run_metis
from spydrnet_physical.util import RoutingRender

logger = logging.getLogger('spydrnet_logs')
sdn.enable_file_logging(LOG_LEVEL='INFO')


def main():
    # Read verilog sources
    proj = "../homogeneous_fabric"
    source_files = []
    source_files += glob.glob(f'{proj}/*_Verilog/routing/*.v')
    source_files += glob.glob(f'{proj}/*_Verilog/sub_module/*.v')
    source_files += glob.glob(
        f'{proj}/FPGA44_Task/CustomModules/standard_cell_p*.v')
    source_files += glob.glob(f'{proj}/FPGA44_Task/CustomModules/ccff.v')

    # Temporary fix to read multiple verilog files
    with tempfile.NamedTemporaryFile(suffix=".v") as fp:
        for eachV in source_files:
            with open(eachV, "r") as fpv:
                fp.write(str.encode(" ".join(fpv.readlines())))
        fp.seek(0)
        netlist = sdn.parse(fp.name)

    # Get cbx_1__1_ module
    cb_module = next(netlist.get_definitions("cbx_1__1_"))
    netlist.top_instance = cb_module

    # Flattern all the mux instances
    for instance in list(cb_module.get_instances('*ipin*')):
        logger.debug(f"Flattening {instance.name}")
        cb_module.flatten_instance(instance)

    # Remove global port and signals
    for signal in ["ccff_tail", "ccff_head", "prog_reset", "cfg_done",
                   "prog_clk", "chanx_left_out", "chanx_right_out"]:
        cb_module.remove_port(next(cb_module.get_ports(signal)))
        cb_module.remove_cable(next(cb_module.get_cables(signal)))

    # Get unwanted instances
    for instance in ["*ASSIG*", ]:
        cb_module.remove_children_from(cb_module.get_instances(instance))

    # Disconnect scan_chain
    for dff in cb_module.get_instances("*_CCDFF_*"):
        port = next(dff.get_ports("*Q*"))
        if port.pins[0].wire:
            port.pins[0].wire.disconnect_pin(port.pins[0])

    for instance in ["*CCDFF*", ]:
        cb_module.remove_children_from(cb_module.get_instances(instance))

    # Split Chanx_ports
    next(cb_module.get_ports("chanx_left_in")).split()
    next(cb_module.get_ports("chanx_right_in")).split()

    cb_module.combine_ports("top_pin_I",
                            list(cb_module.get_ports("*top_grid_*_pin_I*")))
    cb_module.combine_ports("bottom_pin_I",
                            list(cb_module.get_ports("*bottom_grid_*_pin_I*")))

    # Get connectivity graph
    G = cb_module.get_connectivity_network()

    nodes = list(nx.get_node_attributes(G, 'label').values())
    target = nodes.index("port_top_pin_I")
    source = nodes.index("port_bottom_pin_I")
    G.nodes[target]["weight"] = 100
    G.nodes[source]["weight"] = 100

    for p1, p2 in nx.edges(G, [target, source]):
        print(G[p1][p2])
        G[p1][p2]["weight"] = 10
        G[p1][p2]["label"] = "[10]"

    for indx, node_name in enumerate(nodes):
        G.nodes[indx]["label"] = f"{node_name}_[{G.nodes[indx].get('weight', 0)}]"

    nodes = list(nx.get_node_attributes(G, 'label').values())
    vweights = nx.get_node_attributes(G, "weight")

    # n_cuts, membership = pymetis.part_graph(2, adjacency=nx.to_numpy_array(G),
    #                                         vweights=vweights)
    # print(f"n_cuts {n_cuts}")

    # Run using external metis
    write_metis_graph(nx.to_numpy_array(G),
                      eweights=True, vweights=vweights,
                      filename="_partition_exp_remerge.csr")
    membership = run_metis(filename="_partition_exp_remerge.csr", cuts=2,
                           options="-objtype cut -minconn -niter 100 -ncuts 3 ")

    subgraph = pydot.Cluster('part1', label='', bgcolor="#c6ecba"), \
        pydot.Cluster('part2', label='', bgcolor="#f3cfcf")
    partitions = [[], []]

    graph = to_pydot(G)
    for each in subgraph:
        graph.add_subgraph(each)

    for index, color in enumerate(membership):
        node = graph.get_node(str(index))[0]
        node.set_color("red" if color else "green")
        # node.set_shape("rect" if node.get_label(
        # ).startswith("port_") else "circle")
        subgraph[color].add_node(node)
        partitions[color].append(node.get_label())

    for index, color in enumerate(membership):
        if color:
            logger.debug(graph.get_node(str(index))[0])
    logger.debug("")
    for index, color in enumerate(membership):
        if not color:
            logger.debug(graph.get_node(str(index))[0])

    print("============= Parition stats =============")
    f_str = '{:<15s} {:<15} {:<15}'
    print(f_str.format('', 'P1', 'P2'))
    print("==========================================")
    print(f_str.format('chanx_left', len([p for p in partitions[0] if "chanx_left" in p]),
                       len([p for p in partitions[1] if "chanx_left" in p])))
    print(f_str.format('chanx_right', len([p for p in partitions[0] if "chanx_right" in p]),
                       len([p for p in partitions[1] if "chanx_right" in p])))
    print(f_str.format('pin_I', len([p for p in partitions[0] if "pin_I" in p]),
                       len([p for p in partitions[1] if "pin_I" in p])))
    print(f_str.format('CCDFF', len([p for p in partitions[0] if "CCDFF" in p]),
                       len([p for p in partitions[1] if "CCDFF" in p])))
    print(f_str.format('top_grid', len([p for p in partitions[0] if "top_grid" in p]),
                       len([p for p in partitions[1] if "top_grid" in p])))
    print(f_str.format('bottom_grid', len([p for p in partitions[0] if "bottom_grid" in p]),
                       len([p for p in partitions[1] if "bottom_grid" in p])))

    for side in ["top", "bottom"]:
        for pin in range(10):
            p1, p2 = [], []
            tag = f"{side}_ipin_{pin}"
            for i in range(1, 5):
                p1.append(str(len([p for p in partitions[0] if
                                   fnmatch(p, f"*{tag}*l{i}*")])))
                p2.append(str(len([p for p in partitions[1] if
                                   fnmatch(p, f"*{tag}*l{i}*")])))
            print(f_str.format(tag,
                               "-".join(p1) + f" [{sum(map(int,p1))}]",
                               "-".join(p2) + f" [{sum(map(int,p2))}]"))
    with open("_graph.part.0", "w") as fp:
        fp.write("\n".join(partitions[0]))
    with open("_graph.part.1", "w") as fp:
        fp.write("\n".join(partitions[1]))

    sb11_gsb = f"{proj}/FPGA44_gsb/sb_1__1_.xml"
    sb_render = RoutingRender("sb_1__1_", sb11_gsb)
    sw_top = sb_render.report_ipins("top", show=False)
    sw_top[sw_top == 'x'] = "t"
    sw_bottom = sb_render.report_ipins("bottom", show=False)
    sw_bottom[sw_bottom == 'x'] = "b"
    sw = np.vstack([sw_top, sw_bottom])
    sb_render.render_ipin(sw)
    top = [int(e.split("_")[-2]) for e in partitions[0] if "chanx" in e]
    bottom = [int(e.split("_")[-2])+20 for e in partitions[1] if "chanx" in e]
    sb_render.render_ipin(sw[:, top])
    sb_render.render_ipin(sw[:, bottom])

    graph.set_rankdir("LR")
    graph.write_dot('_graph.dot')
    graph.write_png('_graph.png')
    graph.write_svg('_graph.svg')
    sdn.compose(netlist, '_cbx_1__1_extended.v',
                definition_list=["cbx_1__1_"], skip_constraints=True)


if __name__ == "__main__":
    main()
