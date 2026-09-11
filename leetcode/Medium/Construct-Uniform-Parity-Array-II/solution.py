"""
LeetCode: Construct Uniform Parity Array II
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/construct-uniform-parity-array-ii/
"""

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return min(nums1)%2==1 or sum(x&1 for x in nums1)==0
