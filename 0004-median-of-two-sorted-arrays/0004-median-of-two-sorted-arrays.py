class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for optimization
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            # Find partition points in both arrays
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # Find elements around partition points
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Check if we found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If total length is odd
                if (x + y) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                # If total length is even
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            # Adjust search space
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

        raise ValueError("Input arrays are not sorted")