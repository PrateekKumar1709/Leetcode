class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Initialize graph and in-degree map
        adjacency_list = defaultdict(list)
        in_degree = {char: 0 for word in words for char in word}
        
        # Step 2: Build graph
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))
            
            # Check for invalid prefix condition
            if word1[:min_length] == word2[:min_length] and len(word1) > len(word2):
                return ""
            
            # Compare characters and build edges
            for j in range(min_length):
                if word1[j] != word2[j]:
                    adjacency_list[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                    break
        
        # Step 3: Topological sort using BFS
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
        
        while queue:
            char = queue.popleft()
            result.append(char)
            
            for neighbor in adjacency_list[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If result length matches unique characters count, return it; else cycle exists
        if len(result) == len(in_degree):
            return "".join(result)
        else:
            return ""