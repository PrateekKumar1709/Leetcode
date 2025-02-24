class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r: int, c: int) -> None:
            # Base cases: out of bounds or water/visited cell
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == "0"):
                return
            
            # Mark current cell as visited
            grid[r][c] = "0"
            
            # Explore all 4 directions
            dfs(r+1, c)  # down
            dfs(r-1, c)  # up
            dfs(r, c+1)  # right
            dfs(r, c-1)  # left
        
        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1  # Found new island
                    dfs(r, c)    # Mark all connected lands
        
        return islands