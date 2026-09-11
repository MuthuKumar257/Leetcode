"""
LeetCode: Maximum Element After Decreasing and Rearranging
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
"""

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        cnt = 0
        for n in sorted(arr):
            cnt = min(cnt+1, n)
        return cnt
