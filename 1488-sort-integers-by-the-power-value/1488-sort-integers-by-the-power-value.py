class Solution:
    def calculate_power(self, x):
        steps = 0
        while x != 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1
            steps += 1
        return steps
        
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Generate list of (integer, power) pairs
        power_list = [(x, self.calculate_power(x)) for x in range(lo, hi + 1)]
        
        # Sort by power value first, then by integer value
        power_list.sort(key=lambda item: (item[1], item[0]))
        
        # Return the kth integer (1-based index)
        return power_list[k - 1][0]
