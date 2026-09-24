"""
LeetCode: Minimum Days to Score Exactly N Points
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/minimum-days-to-score-exactly-n-points/
"""

class Solution:
    def minDays(self, n: int) -> int:
        dp=[9999]*(n+1)
        dp[0]=0
        for i in range(n+1):
            for k in range(1,int((2*(n-i))**0.5)+1):
                p=k*(k+1)//2
                if i+p<=n:
                    dp[i+p]=min(dp[i+p],dp[i]+k+1)
        return dp[n]-1
