import random
import pygame
from collections import deque

def create_grid(rows, cols):
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            cell = {
                "visited": False,
                "walls": {"top": True, "bottom": True, "left": True, "right": True}
            }
            row.append(cell)
        grid.append(row)
    return grid

def get_unvisited_neighbors(grid, row, col):
    neighbors = []
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        ("top", -1, 0),
        ("bottom", 1, 0),
        ("left", 0, -1),
        ("right", 0, 1),
    ]

    for direction, dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < rows and 0 <= new_col < cols:
            if not grid[new_row][new_col]["visited"]:
                neighbors.append((direction, new_row, new_col))

    return neighbors
# Which wall to remove on the *current* cell, and the matching wall on the *neighbor*
opposite = {"top": "bottom", "bottom": "top", "left": "right", "right": "left"}

def carve_maze(grid, row, col):
    grid[row][col]["visited"] = True
    neighbors = get_unvisited_neighbors(grid, row, col)

    while neighbors:
        direction, new_row, new_col = random.choice(neighbors)

        # only proceed if it's still unvisited (may have changed during recursion)
        if not grid[new_row][new_col]["visited"]:
            grid[row][col]["walls"][direction] = False
            grid[new_row][new_col]["walls"][opposite[direction]] = False

            carve_maze(grid, new_row, new_col)

        neighbors = get_unvisited_neighbors(grid, row, col)
maze = create_grid(5, 5)
carve_maze(maze, 0, 0)

def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])

    # top border
    print(" " + "_" * (cols * 2 - 1))

    for r in range(rows):
        line = "|"
        for c in range(cols):
            cell = grid[r][c]
            line += " " if not cell["walls"]["bottom"] else "_"
            line += " " if not cell["walls"]["right"] else "|"
        print(line)
maze = create_grid(5, 5)
print_grid(maze)

def get_reachable_neighbors(grid, row, col):
    reachable = []
    cell = grid[row][col]

    if not cell["walls"]["top"]:
        reachable.append((row - 1, col))
    if not cell["walls"]["bottom"]:
        reachable.append((row + 1, col))
    if not cell["walls"]["left"]:
        reachable.append((row, col - 1))
    if not cell["walls"]["right"]:
        reachable.append((row, col + 1))

    return reachable

def solve_bfs(grid, start, end):
    queue = deque([start])
    visited = {start}
    came_from = {}

    while queue:
        current = queue.popleft()

        if current == end:
            break

        row, col = current
        for neighbor in get_reachable_neighbors(grid, row, col):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

    # Reconstruct the path by walking backwards from `end` to `start`
    path = []
    current = end
    while current != start:
        if current not in came_from:
            return None  # no path found
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path

def draw_maze(screen, grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = grid[row][col]
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if cell["walls"]["top"]:
                pygame.draw.line(screen, BLACK, (x, y), (x + CELL_SIZE, y), 2)
            if cell["walls"]["bottom"]:
                pygame.draw.line(screen, BLACK, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 2)
            if cell["walls"]["left"]:
                pygame.draw.line(screen, BLACK, (x, y), (x, y + CELL_SIZE), 2)
            if cell["walls"]["right"]:
                pygame.draw.line(screen, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)

def draw_path(screen, path):
    for row, col in path:
        center_x = col * CELL_SIZE + CELL_SIZE // 2
        center_y = row * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, BLUE, (center_x, center_y), CELL_SIZE // 6)


def draw_marker(screen, row, col, color):
    center_x = col * CELL_SIZE + CELL_SIZE // 2
    center_y = row * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, color, (center_x, center_y), CELL_SIZE // 3)

def run_visual():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Generator & Solver")
    clock = pygame.time.Clock()

    start = (0, 0)
    end = (ROWS - 1, COLS - 1)

    grid = create_grid(ROWS, COLS)
    carve_maze(grid, 0, 0)
    path = solve_bfs(grid, start, end)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                grid = create_grid(ROWS, COLS)
                carve_maze(grid, 0, 0)
                path = solve_bfs(grid, start, end)

        screen.fill(WHITE)
        draw_maze(screen, grid)

        if path:
            draw_path(screen, path)
        draw_marker(screen, start[0], start[1], GREEN)
        draw_marker(screen, end[0], end[1], RED)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()




maze = create_grid(5, 5)
carve_maze(maze, 0, 0)
print_grid(maze)

path = solve_bfs(maze, (0, 0), (4, 4))
print(path)


CELL_SIZE = 40
ROWS = 10
COLS = 10

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)


if __name__ == "__main__":
    run_visual()


