class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = (1 << 32) - 1
        
        # Handle negative numbers by converting to unsigned
        n = n & mask if n < 0 else n
        
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count

