from collections import deque


grid = [
    ['P', '.', '.', 'X', '.', '.'],
    ['.', 'X', '.', 'X', 'X', '.'],
    ['.', '.', '.', '.', 'X', '.'],
    ['X', 'X', 'X', '.', 'X', 'X'],
    ['.', '.', '.', '.', '.', 'A']
]


directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(grid):
   
    start = None
    target = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'P':
                target = (i, j)

  
    # BFS
    queue = deque([(start, [])])  
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        # Eğer hedefe ulaşıldıysa, yolu döndürelim
        if current == target:
            return path + [current]

        # Komşuları kontrol edelim
        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                if grid[next_row][next_col] != 'X' and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    queue.append(((next_row, next_col), path + [current]))

    return "Yol bulunamadı!"


path = bfs(grid)

if isinstance(path, list):
    print("En kısa yol: ")
    for step in path:
        print(step)
else:
    print(path)
