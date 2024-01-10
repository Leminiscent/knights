# Logic Puzzles Solver

This Python project provides a framework for solving 'Knights and Knaves' logic puzzles.

## Overview

The project is structured around the concept of logical sentences, with a primary focus on evaluating the truthfulness of statements made by characters in various puzzles. The framework defines a base class `Sentence` and multiple subclasses to represent different logical constructs like symbols, negation, conjunction, disjunction, implication, and biconditional.

## Classes

- `Sentence`: The abstract base class for all logical sentences. It provides essential methods like `evaluate`, `formula`, and `symbols`.
- `Symbol`: Represents a propositional symbol (e.g., "A is a Knight").
- `Not`: Represents logical negation.
- `And`: Represents logical conjunction.
- `Or`: Represents logical disjunction.
- `Implication`: Represents logical implication.
- `Biconditional`: Represents logical biconditional.

Each class has methods to evaluate the truth of the sentence based on a given model, generate a string formula, and retrieve symbols involved.

## Utility Functions

- `model_check`: Checks if a given knowledge base entails a query.
- `check_all`: Helper function for `model_check` to test all combinations of truth assignments.

## Puzzles

Four puzzles are implemented as examples:

- **Puzzle 0**: A paradoxical scenario where a character claims to be both a knight and a knave.
- **Puzzle 1**: Involves two characters, with one claiming they are both knaves.
- **Puzzle 2**: Features two characters, each making a statement about their identity.
- **Puzzle 3**: A more complex scenario involving three characters with interlinked statements.

## Usage

The main function `main` iterates through the defined puzzles, uses the `model_check` function to determine the possible truth assignments that satisfy the puzzle's conditions, and prints the results.

## Requirements

No external libraries are required to run this project, as it only uses standard Python data structures and control flows.

## Running the Project

To run the project, simply execute the Python script. The output will display the solutions for each of the defined puzzles, indicating whether characters are knights or knaves based on their statements.
