class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create adjacency list using defaultdict and priority queues
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
        
        route = []
        
        def dfs(airport):
            # Visit all destinations from current airport
            while graph[airport]:
                # Get lexicographically smallest destination
                next_dest = heapq.heappop(graph[airport])
                dfs(next_dest)
            # Add current airport to route (will be in reverse order)
            route.append(airport)
        
        # Start DFS from JFK
        dfs("JFK")
        
        # Return reversed route for correct order
        return route[::-1]