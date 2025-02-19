class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Edge case: empty lists
        if not nums or not all(nums):
            return []
        
        # Initialize min heap with first element from each list
        # Format: (value, list_index, element_index)
        heap = []
        max_val = float('-inf')
        
        # Add first element from each list to heap
        for i, lst in enumerate(nums):
            if lst:
                heappush(heap, (lst[0], i, 0))
                max_val = max(max_val, lst[0])
        
        # Initialize result range with maximum possible difference
        start, end = float('-inf'), float('inf')
        
        # Process until any list is exhausted
        while len(heap) == len(nums):
            min_val, list_idx, elem_idx = heappop(heap)
            
            # Update range if current range is smaller
            if max_val - min_val < end - start:
                start, end = min_val, max_val
            
            # Add next element from same list if available
            if elem_idx + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][elem_idx + 1]
                heappush(heap, (next_val, list_idx, elem_idx + 1))
                max_val = max(max_val, next_val)
        
        return [start, end]