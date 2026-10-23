class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        time, fresh = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh > 0 and queue:
            length = len(queue)
            for i in range(length):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows)
                        and col in range(cols)
                        and grid[row][col] == 1):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

