class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0  # pointer for 0s (red)
        mid = 0   # pointer for 1s (white)
        right = len(nums) - 1  # pointer for 2s (blue)
        
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
