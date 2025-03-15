class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)  # Convert wordList to a set for O(1) lookups
        if endWord not in wordSet:
            return 0

        # Initialize BFS
        queue = deque([(beginWord, 1)])  # (current_word, transformation_steps)

        while queue:
            current_word, steps = queue.popleft()

            # Try changing each letter in the current word
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + char + current_word[i+1:]

                    # If the next word is the endWord, return the steps + 1
                    if next_word == endWord:
                        return steps + 1

                    # If the next word is in the wordSet, add it to the queue and remove from the set
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, steps + 1))

        return 0  # If no transformation sequence is found