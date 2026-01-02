from src.config import GPA_COL, ID_COL, INTEREST_COLS
from src.similarity import jaccard_similarity

def analyze_gpa(df, groups):
    for i, group in enumerate(groups):
        gpas = df[df[ID_COL].isin(group)][GPA_COL]
        print(f"\nGroup {i+1}:")
        print(f"  Size: {len(gpas)}")
        print(f"  Avg GPA: {gpas.mean():.3f}")
        print(f"  GPA Range: {(gpas.max() - gpas.min()):.3f}")

def interest_overlap(df, groups):
    for i, group in enumerate(groups):
        if len(group) < 2:
            print(f"Group {i+1}: Interest Overlap = 0.000")
            continue

        rows = df[df[ID_COL].isin(group)]
        scores = []
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                scores.append(
                    jaccard_similarity(rows.iloc[i], rows.iloc[j], INTEREST_COLS)
                )
        print(f"Group {i+1}: Interest Overlap = {sum(scores)/len(scores):.3f}")