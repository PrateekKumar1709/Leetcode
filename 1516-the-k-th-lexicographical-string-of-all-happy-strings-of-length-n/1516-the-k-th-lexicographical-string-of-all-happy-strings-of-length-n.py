class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(curr: str):
            # Base case: if current string length equals n
            if len(curr) == n:
                result.append(curr)
                return
            
            # Try adding each possible character
            for c in ['a', 'b', 'c']:
                # Skip if current char matches last char
                if curr and curr[-1] == c:
                    continue
                backtrack(curr + c)
        
        result = []
        backtrack("")
        
        # Return kth string if exists, empty string otherwise
        return result[k-1] if k <= len(result) else ""