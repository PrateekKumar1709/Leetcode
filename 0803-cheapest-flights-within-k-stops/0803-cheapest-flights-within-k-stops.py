class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize distances with infinity
        dist = [math.inf] * n
        dist[src] = 0
        
        # Perform Bellman-Ford for at most k+1 iterations
        for _ in range(k + 1):
            # Temporary copy of distances
            temp_dist = dist[:]
            for from_city, to_city, price in flights:
                # Only update if we can reach from_city
                if dist[from_city] != math.inf:
                    temp_dist[to_city] = min(temp_dist[to_city], dist[from_city] + price)
            # Update distances
            dist = temp_dist
        
        return -1 if dist[dst] == math.inf else dist[dst]