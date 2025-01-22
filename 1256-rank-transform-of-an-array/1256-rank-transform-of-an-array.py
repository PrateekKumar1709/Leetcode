from enum import Enum
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique = sorted(set(arr))
        Rank = Enum('Rank', {str(uni): i+1 for i, uni in enumerate(unique)})
        for i in range(len(arr)):
            arr[i] = Rank[str(arr[i])].value
        
        return arr

