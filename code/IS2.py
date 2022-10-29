from pydoc import describe
import networkx as nx

from code.utils import density

def function_IS2(cluster,graph):

    seed = graph.subgraph(cluster)
    original_density = density(seed)
    increased = True

    while increased:
        N = list(seed.nodes)
        # get adjacent neighbours of vertex in the current cluster and add it to N
        for vertex in seed.nodes:
            adjacent = graph.neighbors(vertex)
            N = list(set(N).union(set(adjacent)))
        for vertex in N:
            original_cluster = seed.nodes
            modified_cluster = []
            if vertex in original_cluster:
                modified_cluster = original_cluster.remove(vertex)
            else:
                modified_cluster = original_cluster.append(vertex)
            
            if density(modified_cluster) > density(seed):
                seed = modified_cluster
        if density(seed) == original_density:
            increased = False
        else:
            original_density = density(seed)
    
    return list(seed.nodes)