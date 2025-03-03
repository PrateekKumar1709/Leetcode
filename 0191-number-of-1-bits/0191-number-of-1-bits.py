class Solution:
    def hammingWeight(self, n: int) -> int:
        # Handle negative numbers by converting to unsigned
        n = n & 0xFFFFFFFF if n < 0 else n
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count

