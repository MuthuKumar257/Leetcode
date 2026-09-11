"""
LeetCode: Squares of a Sorted Array
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/squares-of-a-sorted-array/
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            res.append(i**2)
        res.sort()
        return res
