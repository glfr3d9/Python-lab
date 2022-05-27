import networkx as nx
import matplotlib.pyplot as plt
import floyd_warshall as fw
import convert_adjacency_matrix as cam

with open('inputs.txt', 'r') as inputs:
    global graph
    graph = []

    for line in inputs:
        graph.append(line[:-1].split(', '))


G = nx.DiGraph()
G.add_weighted_edges_from(cam.convert_adjacency_matrix(graph))

pos = nx.planar_layout(G)
nx.draw(G, with_labels='True', pos=pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
path = fw.fw(graph, 0, 7)
print(path)
path = [(path[i], path[i+1]) for i in range(len(path)-1)]
nx.draw_networkx_edges(G, pos=pos, edgelist=path, edge_color='red')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

plt.show()
