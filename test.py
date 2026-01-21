import networkx as nx

# 1. Create an empty graph object
G = nx.Graph()

# 2. Add nodes (they are created automatically when an edge is added)
G.add_node(1)
G.add_nodes_from([2, 3])

# 3. Add edges
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (1, 3)])

# 4. Access information
print(f"Nodes in graph: {list(G.nodes)}")
print(f"Edges in graph: {list(G.edges)}")
print(f"Degree of node 1: {G.degree}")
