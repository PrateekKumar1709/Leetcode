from heapq import heappush, heappop
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        # Cache for memoization
        memo = {}
        
        def calculate_power(x: int) -> int:
            if x == 1:
                return 0
            if x in memo:
                return memo[x]
                
            if x % 2 == 0:
                steps = 1 + calculate_power(x // 2)
            else:
                steps = 1 + calculate_power(3 * x + 1)
                
            memo[x] = steps
            return steps
        
        # Use min heap to maintain k smallest elements
        heap = []
        for num in range(lo, hi + 1):
            power = calculate_power(num)
            heappush(heap, (power, num))
        
        # Pop k-1 elements to get kth element
        for _ in range(k-1):
            heappop(heap)
        
        return heappop(heap)[1]
