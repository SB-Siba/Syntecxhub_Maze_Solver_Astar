# Maze Solver using A* Search Algorithm

## 📌 Project Overview
This project implements a Maze Solver using the A* (A-Star) search algorithm.  
The program finds the shortest path from a start point to a goal point in a grid-based maze while avoiding obstacles.

The project demonstrates core Artificial Intelligence concepts such as heuristic-based search, pathfinding, and optimal decision-making.

---

## 🧠 What is A* Search?
A* is an informed search algorithm that finds the shortest path using the formula:

f(n) = g(n) + h(n)

Where:
- g(n): Cost from the start node to the current node
- h(n): Heuristic estimate from the current node to the goal
- f(n): Total estimated cost

In this project, **Manhattan Distance** is used as the heuristic.

---

## 🧩 Maze Representation
- `0` → Free path
- `1` → Wall / Obstacle
- `S` → Start position
- `G` → Goal position
- `*` → Shortest path

The maze is represented as a 2D grid (list of lists).

---

## ⚙️ How the Algorithm Works
1. Start from the initial position.
2. Explore neighboring cells (up, down, left, right).
3. Use a priority queue to always select the path with the lowest cost.
4. Apply the heuristic to guide the search efficiently.
5. Stop when the goal is reached.
6. If no path exists, return "No path found".

---

## ▶️ How to Run the Project

### Requirements
- Python 3.x (No external libraries required)

### Steps
1. Clone or download the project.
2. Navigate to the project folder.
3. Run the following command:

```bash
python maze_solver.py
