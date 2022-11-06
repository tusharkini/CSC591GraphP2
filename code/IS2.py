
import networkx as nx

from utils import density

def function_IS2(cluster,graph):
    # seed the algorithm with the given cluster
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
            original_cluster = list(seed.nodes)
            modified_cluster = []
            # Adding the new adjacent nodes to be added to the cluster not present already
            if vertex in original_cluster:
                modified_cluster = original_cluster.remove(vertex)
            else:
                modified_cluster = original_cluster.append(vertex)
            # if modified_cluster is empty
            if not modified_cluster:
                modified_cluster = nx.Graph()
            # if the modified_cluster has a greater density then replace the seed
            if density(modified_cluster) > density(seed):
                seed = modified_cluster
        # replace the cluster density if cluster has been modified
        if density(seed) == original_density:
            increased = False
        else:
            original_density = density(seed)
    
    return list(seed.nodes)