class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n  # Initialize result array with -1
        stack = []  # Initialize stack to store indices

        # Iterate through the array twice to cover circular case
        for i in range(2 * n):
            # Use modulo to ensure circular iteration
            idx = i % n
            
            # While stack is not empty and current element is greater than the element at the top of the stack
            while stack and nums[idx] > nums[stack[-1]]:
                # Pop the top element from the stack and update the result array
                top_idx = stack.pop()
                result[top_idx] = nums[idx]
            
            # Push the current index onto the stack
            stack.append(idx)
        
        return result