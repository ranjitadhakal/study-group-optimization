import streamlit as st
import plotly.graph_objects as go
import networkx as nx
from src.data_load import load_data
from src.community_detection import detect_communities
from src.similarity import total_similarity
from src.config import ID_COL, GPA_COL

st.set_page_config(page_title="Study Group Optimizer", layout="wide")

st.title("Study Group Optimizer")
st.markdown("Adjust the similarity threshold to dynamically form study groups")


# Load data
@st.cache_data
def load_cached_data():
    return load_data("data/data.csv")


df = load_cached_data()

# Sidebar for threshold slider


# Build graph with current threshold
def build_graph_with_threshold(df, threshold):
    """Build graph with specified threshold"""
    G = nx.Graph()

    for _, row in df.iterrows():
        G.add_node(row[ID_COL], gpa=row[GPA_COL])

    edge_count = 0
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            sim = total_similarity(df.iloc[i], df.iloc[j])
            if sim >= threshold:
                G.add_edge(df.iloc[i][ID_COL], df.iloc[j][ID_COL], weight=sim)
                edge_count += 1

    return G, edge_count


st.subheader("Network Visualization")

col1, col2 = st.columns([1, 3])
with col1:
    threshold = st.slider(
        "Similarity Threshold",
        min_value=0.0,
        max_value=1.0,
        value=0.4,
        step=0.05,
        help="Adjust threshold to control connection strength between students",
    )
G, edges = build_graph_with_threshold(df, threshold)

# Detect communities
groups, group_map = detect_communities(G)
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", G.number_of_nodes())
col2.metric("Strong Connections", edges)
col3.metric("Study Groups Detected", len(groups))

pos = nx.spring_layout(G, seed=42, k=0.4)

# Prepare edge data
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x,
    y=edge_y,
    mode="lines",
    line=dict(width=0.5, color="#888"),
    hoverinfo="none",
    showlegend=False,
)

# Prepare node data
node_x = []
node_y = []
node_text = []
node_color = []
node_size = []
colors = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
]

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(node)
    node_color.append(colors[group_map[node] % len(colors)])
    node_size.append(15 + (G.nodes[node]["gpa"] + 0.3) * 10)

node_trace = go.Scatter(
    x=node_x,
    y=node_y,
    mode="markers+text",
    text=node_text,
    textposition="top center",
    textfont=dict(color="black"),
    hoverinfo="text",
    hovertext=node_text,
    marker=dict(size=node_size, color=node_color, line_width=2),
    showlegend=False,
)

fig = go.Figure(data=[edge_trace, node_trace])

fig.update_layout(
    title="Hover to interact(Pinch/Scroll to zoom)",
    showlegend=False,
    hovermode="closest",
    margin=dict(b=0, l=0, r=0, t=40),
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    plot_bgcolor="#f8f9fa",
    height=600,
    dragmode="pan",
)

st.plotly_chart(fig, use_container_width=True, config={"scrollZoom": True})


# Display detected groups
st.subheader("Detected Study Groups")
cols = st.columns(2)
with cols[0]:
    st.write("**Group Details:**")
    for i, g in enumerate(groups):
        with st.expander(f"**Group {i+1}** ({len(g)} members)"):
            members_list = sorted(list(g))
            for member in members_list:
                st.write(f"• {member}")

with cols[1]:
    st.write("**Statistics:**")
    st.text(f"Average group size: {len(df) / len(groups) if groups else 0:.1f}")
    st.text(f"Largest group: {max(len(g) for g in groups) if groups else 0} members")
    st.text(f"Smallest group: {min(len(g) for g in groups) if groups else 0} members")
