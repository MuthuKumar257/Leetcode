"""
LeetCode: Stone Game IX
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/stone-game-ix/
"""

class Solution:

    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0] * 3
        for stone in stones:
            cnt[stone % 3] += 1

        if cnt[0] % 2 == 0:
            return cnt[1] >= 1 and cnt[2] >= 1
        else:
            return abs(cnt[1] - cnt[2]) > 2
