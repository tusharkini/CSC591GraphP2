import networkx as nx
# function to get the order of vertices in RaRe using the PageRank algorithm
def order(graph):
    rare = nx.pagerank(graph)
    o = list(k for k, v in sorted(rare.items(), key = lambda item:item[1],reverse=True))
    return o
    #print(o)

def density(graph):
    if nx.number_of_nodes(graph) == 0:
        return 0
    else:
        return float(2 * nx.number_of_edges(graph) / nx.number_of_nodes(graph))

g = nx.Graph()
'''file = "././datasets/dblp/dblp.graph.small"
with open(file) as f:
    next(f)
    for line in f:
        line = line.split()
        g.add_edge(int(line[0]),int(line[1]))
    

order(g)
print(density(g))'''