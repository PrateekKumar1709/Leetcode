class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize distances array with infinity
        # distances[i] represents min cost to reach city i
        distances = [float('inf')] * n
        distances[src] = 0
        
        # For each level of stops (k+1 iterations for k stops)
        for i in range(k + 1):
            # Create temp array to store new distances
            # This prevents using a path with more stops in current iteration
            temp = distances.copy()
            
            # Check all flights
            for from_city, to_city, price in flights:
                # If source city is reachable
                if distances[from_city] != float('inf'):
                    # Update minimum cost to reach to_city
                    temp[to_city] = min(
                        temp[to_city],
                        distances[from_city] + price
                    )
            
            # Update distances for next iteration
            distances = temp
        
        # Return -1 if destination not reachable, else return cost
        return distances[dst] if distances[dst] != float('inf') else -1

