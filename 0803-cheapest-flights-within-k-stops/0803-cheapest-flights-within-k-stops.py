class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize dp array with infinity
        # dp[i][j] represents min cost to reach city j using i stops
        dp = [[float('inf')] * n for _ in range(k + 2)]
        dp[0][src] = 0
        
        # For each number of stops
        for i in range(1, k + 2):
            # Copy previous state
            dp[i][src] = 0
            
            # For each flight
            for from_city, to_city, price in flights:
                # If we can reach the from_city
                if dp[i-1][from_city] != float('inf'):
                    # Update minimum cost to reach to_city
                    dp[i][to_city] = min(dp[i][to_city], 
                                       dp[i-1][from_city] + price)
        
        # Return result if path exists, else -1
        return dp[k+1][dst] if dp[k+1][dst] != float('inf') else -1