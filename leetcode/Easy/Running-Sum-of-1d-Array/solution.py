"""
LeetCode: Running Sum of 1d Array
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/running-sum-of-1d-array/
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        z=[]
        for i in range(1,len(nums)+1):
            z.append(sum(nums[:i]))
        return z
