import networkx as nx
def order(graph):
    rare = nx.pagerank(graph)
    o = list(k for k, v in sorted(rare.items(), key = lambda item:item[1],reverse=True))
    print(o)


g = nx.Graph()
file = "././datasets/dblp/dblp.graph.small"
with open(file) as f:
    next(f)
    for line in f:
        line = line.split()
        g.add_edge(int(line[0]),int(line[1]))
    

order(g)