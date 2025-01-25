class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        max_len = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1
            
            # If current character's count exceeds 2, move left pointer to the right
            while freq[char] > 2:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1
            
            # Update the maximum length
            current_length = right - left + 1
            if current_length > max_len:
                max_len = current_length
        return max_len
        