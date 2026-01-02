from src.data_load import load_data
from src.graph_builder import build_graph
from src.community_detection import detect_communities
from src.analysis import analyze_gpa, interest_overlap
from src.visualization import visualize_graph

df = load_data("data/data.csv")
G, edges = build_graph(df)

print(f"Students: {G.number_of_nodes()}")
print(f"Strong connections: {edges}")

groups, group_map = detect_communities(G)

print("\nDetected Study Groups:")
for i, g in enumerate(groups):
    print(f"Group {i+1} ({len(g)}): {g}")

print("\n GPA ANALYSIS")
analyze_gpa(df, groups)

print("\n INTEREST OVERLAP")
interest_overlap(df, groups)

visualize_graph(G, group_map)