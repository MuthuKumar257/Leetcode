"""
LeetCode: Maximum K to Sort a Permutation
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/maximum-k-to-sort-a-permutation/
"""

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = None
        for i, ele in enumerate(nums):
            if i != ele: # element not in the sorted position
                if res is None:
                    res = ele
                else:
                    res &= ele
        return 0 if res is None else res
