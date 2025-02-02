class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1

        increments = 0
        decrements = 0

        for a, b in zip(nums1, nums2):
            diff = b - a 

            if diff % k != 0:
                return -1

            operations = diff // k
            if operations > 0:
                increments += operations  
            elif operations < 0:
                decrements -= operations  

        return increments if increments == decrements else -1

