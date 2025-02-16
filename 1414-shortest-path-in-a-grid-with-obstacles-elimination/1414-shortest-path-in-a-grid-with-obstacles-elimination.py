from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return -1
            
        rows, cols = len(grid), len(grid[0])
        
        # If k is large enough, we can go in Manhattan distance
        if k >= rows + cols - 2:
            return rows + cols - 2
        
        # (row, col, obstacles_remaining)
        queue = deque([(0, 0, k)])
        visited = {(0, 0, k)}
        steps = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                row, col, remaining = queue.popleft()
                
                if row == rows - 1 and col == cols - 1:
                    return steps
                
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    
                    if (0 <= new_row < rows and 
                        0 <= new_col < cols):
                        
                        new_remaining = remaining - grid[new_row][new_col]
                        state = (new_row, new_col, new_remaining)
                        
                        if new_remaining >= 0 and state not in visited:
                            visited.add(state)
                            queue.append(state)
            
            steps += 1
        
        return -1
