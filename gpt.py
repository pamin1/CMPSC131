def dijkstra(grid, start, finish):
    rows, cols = len(grid), len(grid[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0

    def find_min_distance_node():
        min_distance = float('inf')
        min_node = None
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and distances[r][c] < min_distance:
                    min_distance = distances[r][c]
                    min_node = (r, c)
        return min_node

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while True:
        current = find_min_distance_node()
        if current is None:
            break  # All reachable nodes have been visited
        row, col = current

        if (row, col) == finish:
            return distances[finish[0]][finish[1]]

        visited[row][col] = True

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                new_cost = distances[row][col] + grid[new_row][new_col]
                if new_cost < distances[new_row][new_col]:
                    distances[new_row][new_col] = new_cost

    return float('inf') if distances[finish[0]][finish[1]] == float('inf') else distances[finish[0]][finish[1]]

# Example usage:
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
start = (0, 0)  # Starting at the top-left corner
finish = (2, 2)  # Finishing at the bottom-right corner

print(dijkstra(grid, start, finish))