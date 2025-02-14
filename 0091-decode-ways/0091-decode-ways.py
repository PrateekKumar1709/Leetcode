class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
            
        two_back = 1
        one_back = 1 if s[-1] != '0' else 0
        
        for i in range(len(s) - 2, -1, -1):
            current = 0
            if s[i] != '0':
                current += one_back
                if int(s[i:i+2]) <= 26:
                    current += two_back
            two_back = one_back
            one_back = current
        
        return one_back
