"""
LeetCode: Plus One
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/plus-one/
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p=0
        r=[]
        for i in digits:
            p=p*10+i
        p+=1
        while p>0:
            r.append(p%10)
            p=p//10
        return r[::-1]
