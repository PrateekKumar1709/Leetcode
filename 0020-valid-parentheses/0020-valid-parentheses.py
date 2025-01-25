class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        dict = {']':'[','}':'{',')':'('}
        stack = []

        for i in range(0,len(s)):
            if s[i] in [']',')','}'] and len(stack) != 0 :
                if dict.get(s[i]) == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
                
        if len(stack) == 0:
            return True
        else:
            return False
