import networkx as nx
G = nx.MultiGraph()
G.add_edge(1,2,weight=7)
G.add_edge(1,2,weight=10)
G.add_edge(2,3,weight=9)
#G.add_edge(3,3,weight=0)

# make new graph with sum of weights on each edge
H = nx.Graph()
for u,v,d in G.edges(data=True):
    w = d['weight']
    if H.has_edge(u,v):
        H[u][v]['weight'] += w
    else:
        H.add_edge(u,v,weight=w)

print H.edges(data=True)
#[(1, 2, {'weight': 17}), (2, 3, {'weight': 9})]
print nx.pagerank_numpy(H,alpha=0.85)
#{1: 0.32037465332634, 2: 0.4864858243244209, 3: 0.1931395223492388}