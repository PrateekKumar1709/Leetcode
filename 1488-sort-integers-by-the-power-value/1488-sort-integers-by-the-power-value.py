from functools import cache

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def f(x):
            if x == 1:
                return 0
            if not x % 2:
                return 1 + f(x//2)
            else:
                return 1 + f(3*x + 1)

        res = []
        for i in range(lo, hi + 1):
            res.append((i, f(i)))
        
        res.sort(key=lambda x: x[1])

        return res[k-1][0]
