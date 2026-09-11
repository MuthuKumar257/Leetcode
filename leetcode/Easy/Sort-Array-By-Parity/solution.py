"""
LeetCode: Sort Array By Parity
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/sort-array-by-parity/
"""

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        r=[]
        for i in nums:
            if i%2==0:
                r.append(i)
        for i in nums:
            if i%2!=0:
                r.append(i)
        return r
