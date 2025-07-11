# Pancake Sorting with A\* and BFS

This project implements **heuristic and uninformed search algorithms** (A\* and BFS) to solve the *burnt pancake sorting problem* — a variant of the classic sorting puzzle where each pancake has a burnt (black) side that must be facing down, and the entire stack must be ordered smallest to largest from top to bottom.

> Developed as part of **CISC681 - Artificial Intelligence** coursework at the University of Delaware.

---

## 🔍 Problem Description

Each pancake has:
- A **value**: its relative size (1–4)
- An **orientation**: `'w'` (white side up) or `'b'` (burnt side up)

The objective is to **sort the stack in ascending order**, ensuring all pancakes are oriented white side up. The only allowed operation is flipping the top `n` pancakes.

---

## 🧩 Features

- **Node-based state tracking** with parent lineage, flip history, and cumulative cost
- **BFS (Breadth-First Search)**: guarantees optimal solution in terms of number of moves, but does not use heuristics
- **A\* Search**: uses a custom heuristic (largest out-of-place pancake) to guide search efficiently
- **Tie-breaking**: implemented to ensure stable A\* ordering when nodes have equal cost

---

## 🚀 Usage

```bash
# Input format:
# Enter a string of 8 characters followed by a method flag (b or a)
# Format: <int><w/b><int><w/b><int><w/b><int><w/b><b/a>
# Example:
> 4w2b3w1b a     # Run A* on a stack of 4 pancakes

# Output:
# Sequence of states from start to goal (with costs if using A*)
