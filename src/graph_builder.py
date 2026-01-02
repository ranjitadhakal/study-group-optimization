import networkx as nx
from src.similarity import total_similarity
from src.config import ID_COL, GPA_COL, THRESHOLD

def build_graph(df):
    G = nx.Graph()

    for _, row in df.iterrows():
        G.add_node(row[ID_COL], gpa=row[GPA_COL])

    edge_count = 0
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            sim = total_similarity(df.iloc[i], df.iloc[j])
            if sim >= THRESHOLD:
                G.add_edge(
                    df.iloc[i][ID_COL],
                    df.iloc[j][ID_COL],
                    weight=sim
                )
                edge_count += 1

    return G, edge_count
