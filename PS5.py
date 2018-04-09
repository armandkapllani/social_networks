#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:12:19 2018

@author: armandkapllani
"""

__author__ = "Armand Kapllani, UFlorida Economics"
__email__ = "akapllani@ufl.edu"

import collections
import networkx as nx
import matplotlib.pyplot as plt

#------------------------------------#
# Summary statistics for the network #
#------------------------------------#

# Construct the adjacency matrix 
A = np.array([0,1,1,1,0,0,1,0,1,0,0,0,1,1,0,1,1,1,1,0,1,0,
              0,1,0,0,1,0,0,0,0,0,1,1,0,0]).reshape(6,6)

# Convert the adjacency matrix to graph 
G = nx.Graph(A)


# Information of the network 
print(nx.info(G))

# Vizualize the network 
spring_pos = nx.spring_layout(G)
plt.axis("off")

nx.draw_networkx(G, pos = spring_pos, node_color='deepskyblue', node_size=500, 
                 edge_color='r', width=1)

# Relabel nodes and map the network
mapping={0:'1',1:'2',2:'3', 3:'4', 4:'5', 5:'6'}
H = nx.relabel_nodes(G,mapping)

spring_pos = nx.spring_layout(H)
plt.axis("off")

nx.draw_networkx(H, pos = spring_pos, node_color='deepskyblue', node_size=500, 
                 edge_color='r', width=1)

plt.savefig("network_visualization.png", dpi=500)
plt.show()

# Number of degrees for each vertex
no_degrees = nx.degree(G)


# Average degree of each vertex in the network 
np.array(no_degrees)[:,1].mean()

# Density of the network 
nx.density(G)

# Individual clustering of the six vertices 
clu = nx.clustering(G)
for n,c in sorted(clu.items()):
    print("%d %0.2f"%(n,c))


# Average clustering coefficient 
cc =  nx.clustering(G)
for n,c in sorted(cc.items()):
    print("%d %0.2f"%(n,c))

avg_clust = sum(cc.values()) / len(cc)

# Degree centrality of each vertex 
cen = nx.degree_centrality(G)
for n,c in sorted(cen.items()):
    print("%d %0.2f"%(n,c))

# Closeness centrality 
clo_cen = nx.closeness_centrality(G)
for n,c in sorted(clo_cen.items()):
    print("%d %0.2f"%(n,c))

# Between centrality 
bet_cen = nx.betweenness_centrality(G, normalized=True)
for n,c in sorted(bet_cen.items()):
    print("%d %0.2f"%(n,c))

# Eigenvector centrality (or eigencentrality)
eig_cen = nx.eigenvector_centrality(G)
for n,c in sorted(eig_cen.items()):
    print("%d %0.2f"%(n,c))
    
# Katz-Bonacich centrality
# Find the eigenvalues and their corresponding eigenvectors 
w, v = LA.eig(A)

# alpha: captures how the value being connected to another node 
#        decays with distance where alpha < 1/max(eigen.value)

# beta:  captures a base value on each node 

# Katz-Bonacich Centrality  (alpha = 0.5, beta = 1)
centrality = katz_centrality_numpy(G, 0.5, 1)
for n,c in sorted(centrality.items()):
    print("%d %0.2f"%(n,c))
    
# Katz-Bonacich Centrality  (alpha = 0.333, beta = 1)
centrality = katz_centrality_numpy(G, 1/3, 1)
for n,c in sorted(centrality.items()):
    print("%d %0.2f"%(n,c))


# Degree histogram 
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')

plt.title("Degree Histogram")
plt.ylabel("Number of nodes")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)

# draw graph in inset
plt.axes([0.4, 0.4, 0.5, 0.5])
Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]
pos = nx.spring_layout(G)
plt.axis('off')
nx.draw_networkx_nodes(G, pos, node_size=20)
nx.draw_networkx_edges(G, pos, alpha=0.4)

plt.savefig("degree_histogram.png")
plt.show()
