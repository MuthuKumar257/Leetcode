# Last updated: 9/12/2026, 8:34:02 PM
1class Solution:
2    def minDays(self, n: int) -> int:
3        dp=[9999]*(n+1)
4        dp[0]=0
5        for i in range(n+1):
6            for k in range(1,int((2*(n-i))**0.5)+1):
7                p=k*(k+1)//2
8                if i+p<=n:
9                    dp[i+p]=min(dp[i+p],dp[i]+k+1)
10        return dp[n]-1