class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}
        
        def dfs(start):
            if start == len(s):
                return [[]]
            
            if start in memo:
                return memo[start]
            
            results = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    # Get all valid segmentations for the remaining substring
                    subSegments = dfs(end)
                    for subSegment in subSegments:
                        results.append([word] + subSegment)
            
            memo[start] = results
            return results
        
        segments = dfs(0)
        return [" ".join(segment) for segment in segments]
