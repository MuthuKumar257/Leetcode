"""
LeetCode: Find Missing Elements
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/find-missing-elements/
"""

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=[]
        a,b=min(nums),max(nums)
        for i in range(a,b):
            if i not in nums:
                m.append(i)
        return m
