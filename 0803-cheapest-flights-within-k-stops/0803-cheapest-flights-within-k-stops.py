class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [float('inf')] * n
        distances[src] = 0
        for i in range(k + 1):
            temp = distances.copy()
            for from_city, to_city, price in flights:
                if distances[from_city] != float('inf'):
                    temp[to_city] = min(temp[to_city], distances[from_city] + price)
            distances = temp
        return distances[dst] if distances[dst] != float('inf') else -1
