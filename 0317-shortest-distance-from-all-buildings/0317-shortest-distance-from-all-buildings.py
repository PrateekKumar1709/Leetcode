from collections import deque
from typing import List
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        distances = [[0] * n for _ in range(m)]  # Total distance from all buildings
        reach_count = [[0] * n for _ in range(m)]  # Number of buildings that can reach this cell
        buildings = sum(cell == 1 for row in grid for cell in row)  # Total buildings
        
        def bfs(row: int, col: int) -> None:
            visited = set()
            queue = deque([(row, col, 0)])  # (row, col, distance)
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while queue:
                curr_row, curr_col, dist = queue.popleft()
                
                for dx, dy in directions:
                    new_row, new_col = curr_row + dx, curr_col + dy
                    
                    if (0 <= new_row < m and 0 <= new_col < n and 
                        grid[new_row][new_col] == 0 and 
                        (new_row, new_col) not in visited):
                        
                        distances[new_row][new_col] += dist + 1
                        reach_count[new_row][new_col] += 1
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, dist + 1))
        
        # Perform BFS from each building
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
        
        # Find minimum distance among valid positions
        min_distance = float('inf')
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 0 and 
                    reach_count[i][j] == buildings and 
                    distances[i][j] < min_distance):
                    min_distance = distances[i][j]
        
        return min_distance if min_distance != float('inf') else -1
