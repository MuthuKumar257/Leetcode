"""
LeetCode: Number of People Aware of a Secret
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/number-of-people-aware-of-a-secret/
"""

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0]*n
        dp[0] = 1
        s = 0
        for i in range(delay, n):
            s += dp[i - delay]
            dp[i] = s
            if 0 <= i - forget + 1:
                s -= dp[i-forget+1]
        return(sum(dp[-forget:])) % (10**9+7)
