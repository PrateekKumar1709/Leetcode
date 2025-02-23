class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Calculate total possible strings
        total = 3 * (2 ** (n-1))
        
        # If k is larger than possible strings, return empty
        if k > total:
            return ""
        
        # Adjust k to 0-based indexing
        k -= 1
        
        # Initialize result string
        result = []
        
        # Find first character
        first_char = chr(ord('a') + k // (2 ** (n-1)))
        result.append(first_char)
        k %= (2 ** (n-1))
        
        # Fill remaining positions
        for i in range(n-1):
            # Get available choices (excluding last used character)
            choices = ['a', 'b', 'c']
            choices.remove(result[-1])
            
            # Calculate which choice to use
            idx = k // (2 ** (n-2-i))
            result.append(choices[idx])
            k %= (2 ** (n-2-i))
        
        return ''.join(result)

