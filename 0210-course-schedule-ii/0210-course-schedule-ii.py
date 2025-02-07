class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create adjacency list and in-degree count
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build the graph
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
        
        # Initialize queue with all courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []
        
        # Process courses
        while queue:
            curr_course = queue.popleft()
            result.append(curr_course)
            
            # Reduce in-degree for all dependent courses
            for next_course in adj[curr_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # Return result if all courses are taken, empty array otherwise
        return result if len(result) == numCourses else []
