"""
LeetCode: Smallest Index With Digit Sum Equal to Index
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
"""

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a=nums[i]
            t=0
            while a>0:
                t+=a%10
                a//=10
            if i==t:
                return i
        return -1
