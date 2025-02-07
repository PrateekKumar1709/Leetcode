class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        
        for num in nums:
            # Find the position to insert the current number
            i = bisect_left(dp, num)
            
            # If we should append to the end
            if i == len(dp):
                dp.append(num)
            # Replace the number at position i
            else:
                dp[i] = num
        
        return len(dp)

