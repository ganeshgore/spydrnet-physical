import networkx as nx


def prepare_graph_from_nx(graph):
    xadj = [0]
    adjncy = []
    eweights = []
    nodes = list(range(1, 1+len(graph)))
    for row in graph:
        adj = map(lambda x: (x[0] if bool(x[1]) else 0, x[1]), zip(nodes, row))
        adj = list(filter(lambda x: bool(x[0]), adj))
        adjncy += [a[0] for a in adj]
        eweights += [a[1] for a in adj]
        xadj.append(len(adjncy))
    return xadj, adjncy, eweights
