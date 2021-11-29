import networkx as nx
import numpy as np
import os


def prepare_graph_from_nx(graph):
    """
    This definition converts networkx graph to xadj, adjncy, eweights
    data structures
    """
    xadj = [0]
    adjncy = []
    eweights = []
    nodes = list(range(1, 1+len(graph)))
    for row in graph:
        adj = map(lambda x: (x[0] if bool(x[1])
                             else 0, int(x[1])), zip(nodes, row))
        adj = list(filter(lambda x: bool(x[0]), adj))
        adjncy += [a[0]-1 for a in adj]
        eweights += [a[1] for a in adj]
        xadj.append(len(adjncy))
    return xadj, adjncy, eweights


def write_metis_graph(graph, eweight=False, vweight=False, filename=None):
    """
    This definition write the given netowrkx graph in CSR format for metis
    """
    lines = []
    lines += [f"{len(graph)} {np.count_nonzero(graph)//2}" + " 0" +
              ('1' if vweight else '0') + ('1' if eweight else '0')]
    nodes = list(range(1, 1+len(graph)))
    for indx, row in enumerate(graph):
        line = map(lambda x: (x[0] if bool(x[1])
                              else 0, int(x[1])), zip(nodes, row))
        line = list(filter(lambda x: bool(x[0]), line))
        print(line)
        if eweight:
            lines.append(" ".join([str(e[0])+" "+str(e[1]) for e in line]))
        else:
            lines.append(" ".join([str(e[0]) for e in line]))
        if vweight:
            lines[-1] = f"{vweight.get(indx, 1)} " + lines[-1]
    if filename:
        with open(filename, 'w')as fp:
            fp.write("% Auto-generated\n")
            fp.write("\n".join(lines))
    return lines


def run_metis(filename, cuts, options=""):
    cmd = f"gpmetis {options} {filename} {cuts}"
    print(f"Running [{cmd}]")
    os.system(cmd)
    with open(f"{filename}.part.{cuts}", 'r') as fp:
        memebership = [int(e.strip()) for e in fp.readlines()]
    return memebership
