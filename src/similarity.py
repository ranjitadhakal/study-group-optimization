from src.config import *

def gpa_similarity(gpa1, gpa2):
    return 1 - abs(gpa1 - gpa2)

def jaccard_similarity(row1, row2, columns):
    intersection = 0
    union = 0
    for col in columns:
        if row1[col] == 1 or row2[col] == 1:
            union += 1
            if row1[col] == 1 and row2[col] == 1:
                intersection += 1
    return intersection / union if union else 0

def total_similarity(row1, row2):
    return (
        ALPHA * gpa_similarity(row1[GPA_COL], row2[GPA_COL]) +
        BETA  * jaccard_similarity(row1, row2, SUBJECT_COLS) +
        GAMMA * jaccard_similarity(row1, row2, INTEREST_COLS)
    )
