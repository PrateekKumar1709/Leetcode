class Solution:
    def minGroups(self, intervals):
        events = []

        for start, end in intervals:
            events.append((start, 1)) 
            events.append((end + 1, -1))
            
        events.sort()
        active_intervals = 0
        max_active = 0

        for time, event_type in events:
            active_intervals += event_type
            max_active = max(max_active, active_intervals)

        return max_active
