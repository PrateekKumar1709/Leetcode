class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram_groups = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            anagram_groups[key].append(word)

        return list(anagram_groups.values())
