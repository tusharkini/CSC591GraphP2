from LA import function_LA as LA
from IS2 import function_IS2 as IS2
import sys
import networkx as nx

def main(file):
    #file = sys.argv[1] 
    # create networkx graph from the file path
    graph = nx.Graph()
    with open(file) as f:
        next(f)
        for line in f:
            line = line.split()
            graph.add_edge(int(line[0]),int(line[1]))

    #initialising all the clusters
    clusters_list = LA(graph)
    computed_clusters = []
    #rearranging and computing the clusters
    for cluster in clusters_list:
        computed_clusters.append(IS2(cluster, graph))
    # there might be duplicate clusters due to the nature of the algorithm
    # also the position of elements in the cluster might be different depending on order of addition
    # so get the unique clusters and store them in the file
    print(len(computed_clusters))
    '''final_clusters = []
    for cluster in computed_clusters:
        cluster = sorted(cluster)
        if cluster not in final_clusters:
            final_clusters.append(cluster)'''
    final_clusters = [list(x) for x in set(tuple(x) for x in computed_clusters)]
    print(len(final_clusters))
    with open("output.txt", 'w') as f:
        for fwd in final_clusters:
            line = " ".join(map(str, fwd))
            f.write(line + '\n')


if __name__ == "__main__":
    file = '././datasets'
    main(file)