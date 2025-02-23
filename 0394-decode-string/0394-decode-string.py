class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currNum = 0
        currString = ''
        
        # Iterate through each character in the string
        for c in s:
            # If the character is a digit, accumulate it to form the count
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            # If the character is '[', push the current string and count onto the stack, reset both
            elif c == '[':
                stack.append(currString)
                stack.append(currNum)
                currString = ''
                currNum = 0
            # If the character is ']', pop the previous string and count from the stack, repeat the current string that many times, and append it to the previous string
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                currString = prevString + num * currString
            # If the character is a letter, add it to the current string
            else:
                currString += c
        
        return currString
