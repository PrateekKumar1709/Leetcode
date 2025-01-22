from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Create a dictionary mapping unique values to their ranks
        rank_map = {val: rank for rank, val in enumerate(sorted(set(arr)), 1)}
        
        # Use a list comprehension to create the result
        return [rank_map[num] for num in arr]
