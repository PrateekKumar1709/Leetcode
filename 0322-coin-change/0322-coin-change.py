class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        # Base case: 0 amount needs 0 coins
        dp[0] = 0
        
        # For each amount from 1 to target amount
        for i in range(1, amount + 1):
            # Try each coin
            for coin in coins:
                if coin <= i:
                    # Take minimum of current solution and solution with current coin
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Return -1 if no solution found, else return solution
        return dp[amount] if dp[amount] != amount + 1 else -1
