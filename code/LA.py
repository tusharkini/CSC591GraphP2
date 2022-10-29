from utils import *
import networkx as nx

def function_LA(graph):
    clusters = []
    ordered_vertices = order(graph)
    for vertex in ordered_vertices:
        added = False
        # Iterate through all existing clusters to see if adding vertex increases density or not 
        for j in range(len(clusters)):
            original_density = density(graph.subgraph(clusters[j]))
            modified_density = density(graph.subgraph(clusters[j]+[vertex]))
            if modified_density > original_density:
                added = True
                clusters[j] += [vertex]
            
        # If the vertex cant be added to any existing cluster, create a new one
        if added == False:
            clusters.append([vertex])
        
    return clusters