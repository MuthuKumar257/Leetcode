"""
LeetCode: Search in Rotated Sorted Array
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r=-1
        for i in nums:
            if i==target:
                return nums.index(i)
        return r
