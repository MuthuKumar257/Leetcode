"""
LeetCode: Container With Most Water
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0

        while i < j:
            res = max(res, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res
