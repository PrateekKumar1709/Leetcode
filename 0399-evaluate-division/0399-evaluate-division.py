from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:


        # Build graph
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        
        def dfs(start, end, visited):
            # Base cases
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            # Mark as visited
            visited.add(start)
            
            # Explore neighbors
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result
            
            return -1.0
        
        # Process queries
        return [dfs(start, end, set()) for start, end in queries]
