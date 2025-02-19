from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # Edge case: Empty input
        if not tasks:
            return 0

        # Sort tasks by end times
        tasks.sort(key=lambda x: x[1])

        busy_times = set()
        total_uptime = 0

        for start, end, duration in tasks:
            needed = duration
            # Count how many slots are already occupied by iterating from end time to start time
            for t in range(start, end + 1):
                if t in busy_times:
                    needed -= 1

            # If more time is needed, greedily pick the latest time slots to turn on the computer
            if needed > 0:
                for t in range(end, start - 1, -1):
                    if t not in busy_times:
                        busy_times.add(t)
                        total_uptime += 1 # Increment total uptime counter when adding a new busy time
                        needed -= 1
                        if needed == 0:
                            break
        return len(busy_times)