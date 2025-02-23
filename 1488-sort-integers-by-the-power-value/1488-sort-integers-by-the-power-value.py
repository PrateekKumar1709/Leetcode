class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Cache for memoization to store computed power values
        memo = {}
        
        def calculate_power(x: int) -> int:
            # Base case
            if x == 1:
                return 0
            # Check if already computed
            if x in memo:
                return memo[x]
                
            # Calculate power based on even/odd condition
            if x % 2 == 0:
                steps = 1 + calculate_power(x // 2)
            else:
                steps = 1 + calculate_power(3 * x + 1)
                
            memo[x] = steps
            return steps
        
        # Calculate power for each number and store in list
        power_pairs = []
        for num in range(lo, hi + 1):
            power = calculate_power(num)
            power_pairs.append((power, num))
        
        # Sort by power value first, then by number
        power_pairs.sort()
        
        # Return kth number
        return power_pairs[k-1][1]