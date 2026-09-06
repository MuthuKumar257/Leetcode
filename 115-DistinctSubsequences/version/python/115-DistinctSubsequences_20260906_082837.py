# Last updated: 9/6/2026, 8:28:37 AM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        m, n = len(s), len(t)
4        if m < n:
5            return 0
6        
7        dp = [[0] * (n + 1) for _ in range(m + 1)]
8        for i in range(m + 1):
9            dp[i][n] = 1
10        
11        for i in range(m - 1, -1, -1):
12            for j in range(n - 1, -1, -1):
13                if s[i] == t[j]:
14                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
15                else:
16                    dp[i][j] = dp[i + 1][j]
17        
18        return dp[0][0]