"""
LeetCode: Find All Numbers Disappeared in an Array
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        missing = []

        for i in range(1,len(nums)+1):
            if i not in set_nums:
                missing.append(i)

        return missing
