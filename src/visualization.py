import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(G, group_map):
    plt.figure(figsize=(14, 12))
    pos = nx.spring_layout(G, seed=42, k=0.4)

    colors = plt.cm.tab10.colors
    node_colors = [colors[group_map[n] % len(colors)] for n in G.nodes()]
    node_sizes = [1200 * (G.nodes[n]['gpa'] + 0.3) for n in G.nodes()]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes)
    nx.draw_networkx_edges(G, pos, alpha=0.4)
    nx.draw_networkx_labels(G, pos, font_size=8)

    plt.title("📘 Study Group Formation Based on Similarity")
    plt.axis("off")
    plt.show()
