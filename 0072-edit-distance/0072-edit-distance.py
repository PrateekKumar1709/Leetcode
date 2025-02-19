class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Get lengths of both strings
        m, n = len(word1), len(word2)
        
        # If one string is empty, return length of other string
        if m == 0: return n
        if n == 0: return m
        
        # Create a DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize first row and column
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    # If characters match, no operation needed
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Take minimum of three operations
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # deletion
                        dp[i][j-1],    # insertion
                        dp[i-1][j-1]   # replacement
                    )
        
        return dp[m][n]