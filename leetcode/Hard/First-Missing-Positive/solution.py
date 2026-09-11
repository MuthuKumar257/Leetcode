"""
LeetCode: First Missing Positive
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/first-missing-positive/
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        a=1
    
        while a in s:
            a+=1
        return a
