"""
LeetCode: How Many Numbers Are Smaller Than the Current Number
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            b=0
            for j in nums:
                if i>j:
                    b+=1
            a.append(b)
        return a
