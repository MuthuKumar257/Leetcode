"""
LeetCode: Stone Game IV
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/stone-game-iv/
"""

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, isqrt(i) + 1):
                if not dp[i - j * j]:
                    dp[i] = True
                    break
        return dp[n]
