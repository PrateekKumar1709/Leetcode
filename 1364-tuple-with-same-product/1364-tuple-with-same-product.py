from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:  # Edge case: array too small
            return 0
            
        # Hash map to store product frequencies
        product_freq = defaultdict(int)
        
        # Calculate products for all possible pairs
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_freq[product] += 1
        
        result = 0
        # Calculate valid tuples for each product
        for freq in product_freq.values():
            if freq > 1:
                # For each pair of pairs with same product
                # We can form 8 different arrangements
                result += freq * (freq - 1) * 4
                
        return result
