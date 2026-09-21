# Maze Generator & Solver

A Python project that procedurally generates a random maze using recursive backtracking, then solves it using Breadth-First Search (BFS) to find the shortest path — visualized in real time with Pygame.

## Features

- **Random maze generation** using recursive backtracking, guaranteeing a unique path between any two cells
- **Shortest-path solving** using BFS, visualized as a connected trail from start to end
- **Interactive regeneration** — press `R` at any time to instantly generate and solve a brand new maze
- Clean grid-based rendering built with Pygame

## How It Works

1. **Generation** — Starting from the top-left cell, the algorithm recursively visits a random unvisited neighbor, knocking down the wall between them, and backtracks automatically when it hits a dead end. This produces a "perfect maze" with exactly one path between any two points.
2. **Solving** — The maze is treated as a graph, where each cell is a node connected to its neighbors wherever no wall exists. BFS explores this graph outward from the start cell until it reaches the end, guaranteeing the shortest possible path.
3. **Visualization** — Pygame renders the maze walls as black lines, the solved path as blue dots, and the start/end points as green/red markers.

## Tech Stack

- Python 3
- Pygame

## Installation & Running

```bash
pip install pygame
python maze.py
```

## Controls

| Key | Action |
|-----|--------|
| `R` | Generate a new random maze and re-solve it |
| Close window | Exit the program |

## Project Structure

```
maze.py    # All project logic: grid creation, maze generation, BFS solving, and Pygame visualization
```

## Concepts Demonstrated

- Recursion and backtracking
- Graph representation and traversal (BFS)
- 2D grid/matrix manipulation
- Event-driven programming with Pygame

## Possible Future Improvements

- Animate the generation process step-by-step instead of generating instantly
- Add DFS as a second solving option to compare against BFS
- Add weighted cells and implement Dijkstra's algorithm or A* search
- Let the user click to set custom start/end points
