"""
LeetCode: Maximum Total Subarray Value I
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/maximum-total-subarray-value-i/
"""

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        a=max(nums)
        b=min(nums)
        return (a-b)*k
