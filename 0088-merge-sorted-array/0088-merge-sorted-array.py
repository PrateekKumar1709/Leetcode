class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:n] = nums2[:n]
            return

        m1 = m - 1
        m2 = m + n - 1
        n1 = n - 1

        while (n1 >= 0):
            if m1 >= 0 and nums1[m1] > nums2[n1]:
                nums1[m2] = nums1[m1]
                m1 -= 1
                m2 -= 1
            else:
                nums1[m2] = nums2[n1]
                n1 -= 1
                m2 -= 1
        
        return

