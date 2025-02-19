class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Create a set for O(1) lookup
        wordSet = set(wordList)
        
        # Create pattern to word mapping
        # For example, for "hit": "*it", "h*t", "hi*"
        pattern_map = defaultdict(list)
        word_len = len(beginWord)
        
        # Build pattern map for all words including beginWord
        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_map[pattern].append(word)
        
        # BFS queue with word and level
        queue = deque([(beginWord, 1)])
        visited = {beginWord}  # Track visited words
        
        while queue:
            current_word, level = queue.popleft()
            
            # Generate all possible patterns for current word
            for i in range(word_len):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                
                # Check all words matching this pattern
                for next_word in pattern_map[pattern]:
                    if next_word == endWord:
                        return level + 1
                    
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
        
        return 0