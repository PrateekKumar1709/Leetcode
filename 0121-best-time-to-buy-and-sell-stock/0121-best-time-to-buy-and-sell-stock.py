class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Handle edge cases
        if not prices or len(prices) < 2:
            return 0
        
        # Initialize variables to track minimum price and maximum profit
        min_price = float('inf')
        max_profit = 0
        
        # Iterate through prices
        for price in prices:
            # Update minimum price if current price is lower
            min_price = min(min_price, price)
            # Calculate potential profit and update maximum if higher
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
        
        return max_profit