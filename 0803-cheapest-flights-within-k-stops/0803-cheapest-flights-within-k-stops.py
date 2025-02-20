class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        prices = [INF] * n
        prices[src] = 0
        
        # We need k+1 iterations since k stops means k+1 edges
        for i in range(k + 1):
            # Create a temporary array to store updates
            temp_prices = prices.copy()
            
            # Check each flight
            for from_city, to_city, price in flights:
                # If source city is reachable
                if prices[from_city] != INF:
                    # Update price if we find a cheaper path
                    temp_prices[to_city] = min(
                        temp_prices[to_city], 
                        prices[from_city] + price
                    )
            
            prices = temp_prices
        
        # Return -1 if destination is unreachable, else return the price
        return -1 if prices[dst] == INF else prices[dst]