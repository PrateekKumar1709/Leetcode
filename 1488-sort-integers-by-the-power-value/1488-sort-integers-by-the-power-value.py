class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power_value(x):
            steps = 0
            while x != 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1
                steps += 1
            return steps

        return sorted(range(lo, hi+1), key=lambda x: (power_value(x), x))[k-1]
