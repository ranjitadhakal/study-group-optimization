# Similarity weights (must sum to 1.0)
# Binary features (Jaccard) maintain group separation
# Increased continuous scores for Interest, Habit, Social
GPA_WEIGHT = 0.04
HABIT_WEIGHT = 0.13
INTEREST_WEIGHT = 0.13
CONFIDENCE_WEIGHT = 0.04
STYLE_TOOLS_WEIGHT = 0.04
SOCIAL_WEIGHT = 0.13
SUBJECT_WEIGHT = 0.25
SUBJECT_INTEREST_WEIGHT = 0.27
THRESHOLD = 0.4

ID_COL = "What does everyone know you as? (Your usual name/nickname!)"
GPA_COL = "gpa ( norm)"
HABIT_COL = "habits score"
INTEREST_SCORE_COL = "interersts score"
CONFIDENCE_COL = "confidence score"
STYLE_TOOLS_COL = "methods score"
SOCIAL_COL = "social score"

SUBJECT_COLS = [
    "Graph",
    "Algo",
    "Opera",
    "H-C-I",
    "S.A.D",
    "Compiler",
    "ethics",
    "embedd",
    "graphics",
    "HCI",
    "SAD",
    "CD",
    "ISE",
    "GT",
    "AC",
    "CG",
    "ES",
    "OR",
]

INTEREST_COLS = [
    "Reading",
    "Watching_Videos",
    "Solving_Problems",
    "Note_Making",
    "Teaching_Others",
    "Group_Discussions",
    "Drawing_Diagrams",
    "YT",
    "GPT",
    "Slides",
    "PDF",
    "docs",
    "notion",
]
