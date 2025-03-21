from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.length: int = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict: Dict[str, List[str]] = defaultdict(list)

    def visitWordNode(
        self,
        queue: Deque[str],
        visited: Dict[str, int],
        others_visited: Dict[str, int],
    ) -> Any:
        queue_size: int = len(queue)
        for _ in range(queue_size):
            current_word: str = queue.popleft()
            for i in range(self.length):
                # Intermediate words for current word
                intermediate_word: str = (
                    current_word[:i] + "*" + current_word[i + 1 :]
                )

                # Next states are all the words which share the same intermediate state.
                for word in self.all_combo_dict[intermediate_word]:
                    # If the intermediate state/word has already been visited from the
                    # other parallel traversal this means we have found the answer.
                    if word in others_visited:
                        return visited[current_word] + others_visited[word]
                    if word not in visited:
                        # Save the level as the value of the dictionary, to save number of hops.
                        visited[word] = visited[current_word] + 1
                        queue.append(word)

        return None

    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        if (
            endWord not in wordList
            or not endWord
            or not beginWord
            or not wordList
        ):
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

        # Queues for birdirectional BFS
        queue_begin: Deque[str] = collections.deque(
            [beginWord]
        )  # BFS starting from beginWord
        queue_end: Deque[str] = collections.deque(
            [endWord]
        )  # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin: Dict[str, int] = {beginWord: 1}
        visited_end: Dict[str, int] = {endWord: 1}
        ans: Any = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # Progress forward one step from the shorter queue
            if len(queue_begin) <= len(queue_end):
                ans = self.visitWordNode(
                    queue_begin, visited_begin, visited_end
                )
            else:
                ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0