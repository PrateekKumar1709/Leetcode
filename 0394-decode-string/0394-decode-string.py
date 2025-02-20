class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ''
        
        # Iterate through each character in the input string
        for c in s:
            # If the character is a digit, update the current number
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            # If the character is a letter, append it to the current string
            elif c.isalpha():
                curr_str += c
            # If the character is '[', push the current string and number onto the stack
            elif c == '[':
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = ''
                curr_num = 0
            # If the character is ']', pop from the stack and repeat the current string
            elif c == ']':
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + num * curr_str
        
        return curr_str
