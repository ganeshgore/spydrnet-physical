import networkx as nx
import numpy as np


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
        adjncy += [a[0] for a in adj]
        eweights += [a[1] for a in adj]
        xadj.append(len(adjncy))
    return xadj, adjncy, eweights


def write_metis_graph(graph, weight=False, filename=None):
    """
    This definition write the given netowrkx graph in CSR format for metis
    """
    lines = []
    lines += [f"{len(graph)} {np.count_nonzero(graph)//2}"]
    nodes = list(range(1, 1+len(graph)))
    for row in graph:
        line = map(lambda x: (x[0] if bool(x[1])
                              else 0, int(x[1])), zip(nodes, row))
        line = list(filter(lambda x: bool(x[0]), line))
        if weight:
            lines.append(" ".join([str(e[0]-1)+" "+str(e[1]) for e in line]))
        else:
            lines.append(" ".join([str(e[0]-1) for e in line]))
    if filename:
        with open(filename, 'w')as fp:
            fp.writelines(lines)
    return lines
