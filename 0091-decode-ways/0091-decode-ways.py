class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string has one way to decode
        dp[1] = 1 if s[0] != '0' else 0  # Base case: single digit

        for i in range(2, n + 1):
            # Check single digit decode (1-9)
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # Check two digit decode (10-26)
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
