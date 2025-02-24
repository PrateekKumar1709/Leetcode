class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Initialize result as -1 (for when no valid pairs exist)
        result = -1
        
        # Create defaultdict to store maximum number for each digit sum
        digit_sum_map = defaultdict(int)
        
        # Iterate through each number in the array
        for num in nums:
            # Calculate sum of digits
            digit_sum = sum(int(digit) for digit in str(num))
            
            # If we've seen this digit sum before
            if digit_sum_map[digit_sum] != 0:
                # Update result if current pair sum is larger
                result = max(result, num + digit_sum_map[digit_sum])
            
            # Update maximum number for this digit sum
            digit_sum_map[digit_sum] = max(digit_sum_map[digit_sum], num)
        
        return result