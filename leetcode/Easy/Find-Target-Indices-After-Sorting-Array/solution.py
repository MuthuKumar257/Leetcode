"""
LeetCode: Find Target Indices After Sorting Array
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/find-target-indices-after-sorting-array/
"""

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        return [i for i in range(len(nums)) if nums[i]==target]
