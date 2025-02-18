class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        
        m, n = len(board), len(board[0])
        
        def dfs(row, col, index):
            # Base case: if we've matched all characters
            if index == len(word):
                return True
                
            # Check bounds and current character match
            if (row < 0 or row >= m or col < 0 or col >= n or 
                board[row][col] != word[index]):
                return False
            
            # Mark as visited by changing to special character
            temp = board[row][col]
            board[row][col] = '#'
            
            # Try all four directions
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + dx, col + dy
                if dfs(new_row, new_col, index + 1):
                    return True
            
            # Backtrack: restore the cell
            board[row][col] = temp
            return False
        
        # Try each cell as starting point
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
