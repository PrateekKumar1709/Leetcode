class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge cases
        if not s or not t or len(s) < len(t):
            return ""
        
        # Initialize frequency maps
        t_freq = {}
        window_freq = {}
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
            window_freq[char] = 0
        
        # Initialize variables
        required = len(t_freq)  # Number of unique chars needed
        current = 0  # Number of chars currently satisfied
        left = 0  # Left pointer of window
        min_window = float('inf')  # Length of minimum window
        result = ""  # Result string
        
        # Iterate through string s with right pointer
        for right in range(len(s)):
            # Get current character
            char = s[right]
            
            # Update window frequency
            if char in t_freq:
                window_freq[char] += 1
                if window_freq[char] == t_freq[char]:
                    current += 1
            
            # Try to minimize window when all chars are found
            while current == required:
                # Update result if current window is smaller
                if right - left + 1 < min_window:
                    min_window = right - left + 1
                    result = s[left:right + 1]
                
                # Remove leftmost character
                char = s[left]
                if char in t_freq:
                    window_freq[char] -= 1
                    if window_freq[char] < t_freq[char]:
                        current -= 1
                left += 1
        
        return result
      