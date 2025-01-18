from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0
        dq = deque([(0, 0, 0)])  # (row, col, current_cost)

        while dq:
            x, y, curr_cost = dq.popleft()
            
            if x == m - 1 and y == n - 1:
                return curr_cost

            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = curr_cost + (1 if grid[x][y] != i + 1 else 0)
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        if grid[x][y] == i + 1:
                            dq.appendleft((nx, ny, new_cost))  # prioritize no-cost moves
                        else:
                            dq.append((nx, ny, new_cost))

        return cost[m - 1][n - 1]
