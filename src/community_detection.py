from collections import defaultdict
import community as community_louvain

def detect_communities(G):
    partition = community_louvain.best_partition(G, weight="weight")

    groups = defaultdict(list)
    for student, cid in partition.items():
        groups[cid].append(student)

    group_map = {}
    for cid, members in groups.items():
        for student in members:
            group_map[student] = cid

    return list(groups.values()), group_map
