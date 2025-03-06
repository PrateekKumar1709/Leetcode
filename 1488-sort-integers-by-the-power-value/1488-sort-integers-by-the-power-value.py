
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
        # Calculate power values for all integers in the range
        power_values = [(x, self.calculate_power(x)) for x in range(lo, hi + 1)]
        
        # Sort the integers by their power values in ascending order
        # If two integers have the same power value, sort them by their integer value
        sorted_power_values = sorted(power_values, key=lambda x: (x[1], x[0]))
        
        # Return the kth integer
        return sorted_power_values[k - 1][0]