from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        if not tasks:
            return 0

        # Sort tasks by end times
        tasks.sort(key=lambda x: x[1])

        timeline = []  # List to store the times when the computer is on
        total_uptime = 0

        for start, end, duration in tasks:
            # Count how many seconds the computer is already on during this task's interval
            covered_time = 0
            for time in timeline:
                if start <= time <= end:
                    covered_time += 1

            # If the task is already covered, move on
            if covered_time >= duration:
                continue

            # Turn on the computer for the remaining duration, prioritizing the end
            remaining_duration = duration - covered_time
            for i in range(end, start - 1, -1):  # Iterate backwards from end to start
                if remaining_duration == 0:
                    break
                if i not in timeline:
                    timeline.append(i)
                    total_uptime += 1
                    remaining_duration -= 1

        return len(set(timeline))