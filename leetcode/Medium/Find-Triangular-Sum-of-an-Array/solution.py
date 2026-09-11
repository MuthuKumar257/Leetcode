"""
LeetCode: Find Triangular Sum of an Array
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/find-triangular-sum-of-an-array/
"""

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        l1 = []

        while len(nums) != 1:
            for i in range(len(nums)-1):
                number = (nums[i] + nums[i+1]) % 10
                l1.append(number)
            nums = l1[:]
            l1 = []
        return nums[0]
