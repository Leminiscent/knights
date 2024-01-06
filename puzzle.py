from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # If A is a Knight, then A must be both a Knight and a Knave (impossible)
    Biconditional(AKnight, And(AKnight, AKnave)),
    # If A is a Knave, then it's not the case that A is both a Knight and a Knave
    Biconditional(AKnave, Not(And(AKnight, AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Defining character identities as either knights or knaves
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    # Interpretation of A's statement
    # If A is a knight, then both A and B are knaves - contradiction, thus A cannot be a knight
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave, then not both A and B are knaves
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Defining character identities as either knights or knaves
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    # Interpretation of A's statement
    # If A is a knight, then B is also a knight
    Implication(AKnight, BKnight),
    # If A is a knave, then B is a knight
    Implication(AKnave, BKnight),
    # Interpretation of B's statement
    # If B is a knight, then A is a knave
    Implication(BKnight, AKnave),
    # If B is a knave, then A is a knave
    Implication(BKnave, AKnave),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Defining character identities as either knights or knaves
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    # Interpretation of B's statements
    # If B is a knight, then A did not say 'I am a knave' (thus A is a knight)
    Implication(BKnight, AKnight),
    # If B is a knave, A could be a knight or a knave
    # If B is a knight, then C is a knave
    Implication(BKnight, CKnave),
    # If B is a knave, then C is a knight
    Implication(BKnave, CKnight),
    # Interpretation of C's statement
    # If C is a knight, then A is a knight
    Implication(CKnight, AKnight),
    # If C is a knave, then A is a knave
    Implication(CKnave, AKnave),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
