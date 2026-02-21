import queue

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "X", "#", "#"],
]


def print_maze(maze):
    for row in maze:
        print(" - ".join(row))


print_maze(maze)


def find_start(maze):
    for i, row in enumerate(maze):
        for i_col, col in enumerate(row):
            if maze[i][i_col] == "O":
                return i, i_col
    return None


def find_path(maze):
    start_pos = find_start(maze)
    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()

    while not q.empty():
        (row, col), path = q.get()

        print(path)

        if maze[row][col] == "X":
            return path

        neighbors = neighbors_(maze, row, col)

        for dec in neighbors:
            if dec in visited:
                continue
            r,c = dec
            if maze[r][c] == "#":
                continue

            new_path = path + [dec]
            q.put((dec,new_path))
            visited.add(dec)


def neighbors_(maz, row, col):
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in neighbors:
        r, c = row + dr, col + dc
        if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != "#":
            neighbors.append((r, c))
    return neighbors

result_path = find_path(maze)
if result_path:
    print(f"تم إيجاد الطريق! طول المسار: {len(result_path)} خطوة.")
    print(result_path)
else:
    print("لا يوجد مسار للوصول إلى الهدف.")
