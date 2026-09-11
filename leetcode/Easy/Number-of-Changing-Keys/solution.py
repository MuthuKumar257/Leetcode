"""
LeetCode: Number of Changing Keys
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/number-of-changing-keys/
"""

class Solution:
    def countKeyChanges(self, s: str, ans = 0) -> int:

        for a,b in pairwise(s.lower()):
            ans+= a != b

        return ans
