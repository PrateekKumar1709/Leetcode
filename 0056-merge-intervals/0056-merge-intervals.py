class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Handle empty input
        if not intervals:
            return []
        
        # Sort intervals by start time
        # This ensures overlapping intervals will be adjacent
        intervals.sort(key=lambda x: x[0])
        
        # Initialize result with first interval
        result = [intervals[0]]
        
        # Iterate through remaining intervals
        for current in intervals[1:]:
            last_merged = result[-1]
            
            # If current interval overlaps with last result interval
            if current[0] <= last_merged[1]:
                # Merge by updating end time to maximum of both ends
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add current interval to result
                result.append(current)
        
        return result