from collections import deque
from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Get dimensions of the grid
        n = len(grid)
        
        # Helper function to find first island using DFS
        def find_first_island():
            def dfs(i: int, j: int, island: set):
                if (i < 0 or i >= n or j < 0 or j >= n or 
                    grid[i][j] == 0 or (i,j) in island):
                    return
                
                island.add((i,j))
                # Check all 4 directions
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    dfs(i + di, j + dj, island)
            
            # Find first 1 in the grid
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        first_island = set()
                        dfs(i, j, first_island)
                        return first_island
        
        # Find first island
        first_island = find_first_island()
        
        # BFS queue with initial positions and distance 0
        queue = deque((i, j, 0) for i, j in first_island)
        visited = set(first_island)
        
        # BFS to find shortest path to second island
        while queue:
            i, j, distance = queue.popleft()
            
            # Check all 4 directions
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                
                if (0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited):
                    if grid[ni][nj] == 1:
                        return distance
                    visited.add((ni, nj))
                    queue.append((ni, nj, distance + 1))
        
        return -1  # Should never reach here given problem constraints
