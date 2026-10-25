"""
LeetCode: Set Mismatch
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/set-mismatch/
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))

        duplicate = actual_sum - unique_sum

        missing = n * (n + 1) // 2 - unique_sum

        return [duplicate, missing]
