from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Edge cases
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        
        # If k is large enough, we can go directly
        if k >= m + n - 2:
            return m + n - 2
        
        # BFS queue: (row, col, obstacles_remaining, steps)
        queue = deque([(0, 0, k, 0)])
        # Visited set: (row, col, obstacles_remaining)
        visited = {(0, 0, k)}
        
        # All possible directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            row, col, obstacles, steps = queue.popleft()
            
            # Check if reached destination
            if row == m - 1 and col == n - 1:
                return steps
            
            # Try all four directions
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                # Check if new position is valid
                if (0 <= new_row < m and 0 <= new_col < n):
                    new_obstacles = obstacles - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_obstacles)
                    
                    # If we can move to this position and haven't visited it
                    if new_obstacles >= 0 and new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_row, new_col, new_obstacles, steps + 1))
        
        return -1

