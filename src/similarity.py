from src.config import *


def gpa_similarity(gpa1, gpa2):
    """Normalized GPA similarity: 1 - absolute difference"""
    return 1 - abs(gpa1 - gpa2)


def habit_similarity(habit1, habit2):
    """Habit score similarity: 1 - absolute difference"""
    return 1 - abs(habit1 - habit2)


def interest_similarity(interest1, interest2):
    """Interest score similarity: 1 - absolute difference"""
    return 1 - abs(interest1 - interest2)


def confidence_similarity(conf1, conf2):
    """Confidence score similarity: 1 - absolute difference"""
    return 1 - abs(conf1 - conf2)


def style_tools_similarity(style1, style2):
    """Style and tools score similarity: 1 - absolute difference"""
    return 1 - abs(style1 - style2)


def social_similarity(social1, social2):
    """Social score similarity: 1 - absolute difference"""
    return 1 - abs(social1 - social2)


def jaccard_similarity(row1, row2, columns):
    """Jaccard similarity for binary features"""
    intersection = 0
    union = 0
    for col in columns:
        if row1[col] == 1 or row2[col] == 1:
            union += 1
            if row1[col] == 1 and row2[col] == 1:
                intersection += 1
    return intersection / union if union else 0


def total_similarity(row1, row2):
    """Calculate total similarity score combining all factors"""
    gpa_score = gpa_similarity(row1[GPA_COL], row2[GPA_COL])
    habit_score = habit_similarity(row1[HABIT_COL], row2[HABIT_COL])
    interest_score = interest_similarity(
        row1[INTEREST_SCORE_COL], row2[INTEREST_SCORE_COL]
    )
    confidence_score = confidence_similarity(row1[CONFIDENCE_COL], row2[CONFIDENCE_COL])
    style_tools_score = style_tools_similarity(
        row1[STYLE_TOOLS_COL], row2[STYLE_TOOLS_COL]
    )
    social_score = social_similarity(row1[SOCIAL_COL], row2[SOCIAL_COL])

    # Binary feature comparisons (create strong differentiation)
    subject_score = jaccard_similarity(row1, row2, SUBJECT_COLS)
    interest_cols_score = jaccard_similarity(row1, row2, INTEREST_COLS)

    return (
        GPA_WEIGHT * gpa_score
        + HABIT_WEIGHT * habit_score
        + INTEREST_WEIGHT * interest_score
        + CONFIDENCE_WEIGHT * confidence_score
        + STYLE_TOOLS_WEIGHT * style_tools_score
        + SOCIAL_WEIGHT * social_score
        + SUBJECT_WEIGHT * subject_score
        + SUBJECT_INTEREST_WEIGHT * interest_cols_score
    )
