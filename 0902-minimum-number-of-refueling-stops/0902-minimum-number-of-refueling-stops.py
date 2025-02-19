class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Edge case: Can reach target without refueling
        if startFuel >= target:
            return 0
        
        # Edge case: Can't reach first station or target with start fuel
        if stations and startFuel < stations[0][0]:
            return -1
        
        # Initialize variables
        stops = 0  # number of stops made
        curr_fuel = startFuel  # current fuel available
        curr_pos = 0  # current position
        fuel_heap = []  # max heap to store available fuel amounts
        station_idx = 0  # current station index
        
        # Continue while we haven't reached the target
        while curr_pos < target:
            # Add all reachable stations' fuel to our heap
            while station_idx < len(stations) and stations[station_idx][0] <= curr_pos + curr_fuel:
                # Note: we use negative fuel for max heap in Python's min heap
                heappush(fuel_heap, -stations[station_idx][1])
                station_idx += 1
            
            # If we can reach target, return stops
            if curr_pos + curr_fuel >= target:
                return stops
            
            # If no stations reachable and heap empty, we can't reach target
            if not fuel_heap:
                return -1
            
            # Take the maximum fuel from heap
            curr_fuel += -heappop(fuel_heap)
            stops += 1
        
        return stops