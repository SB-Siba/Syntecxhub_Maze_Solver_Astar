import heapq

# Maze representation
# 0 = free path, 1 = wall
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0]
]

start = (0, 0)
goal = (3, 4)

# Heuristic function (Manhattan Distance)
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# Get valid neighboring cells
def get_neighbors(position, maze):
    neighbors = []
    row, col = position

    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in moves:
        new_row = row + dx
        new_col = col + dy

        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
            if maze[new_row][new_col] == 0:
                neighbors.append((new_row, new_col))

    return neighbors

# A* Algorithm
def astar(maze, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(current, maze):
            temp_g = g_score[current] + 1

            if neighbor not in g_score or temp_g < g_score[neighbor]:
                g_score[neighbor] = temp_g
                f = temp_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f, neighbor))
                came_from[neighbor] = current

    return None

# Display maze with path
def display_maze(maze, path, start, goal):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            cell = (i, j)

            if cell == start:
                print("S", end=" ")
            elif cell == goal:
                print("G", end=" ")
            elif path and cell in path:
                print("*", end=" ")
            elif maze[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

# Run the algorithm
path = astar(maze, start, goal)

if path:
    print("Shortest path found:")
    print(path)
    print("\nMaze Visualization:\n")
    display_maze(maze, path, start, goal)
else:
    print("No path found")
