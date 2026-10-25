"""
LeetCode: Missing Number
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/missing-number/
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=max(nums)
        for i in range(a+1):
            if i in nums:
                pass
            else:
                return i
        return a+1
