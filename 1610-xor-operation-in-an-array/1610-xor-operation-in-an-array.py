class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s1=[]
        r = 0
        for i in range(n):
            s=start+(i*2)
            s1.append(s)
        for i in range(len(s1)):
            r = r ^ s1[i]
        return r
            