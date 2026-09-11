"""
LeetCode: Divisible and Non-divisible Sums Difference
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        d=[]
        nd=[]
        for i in range(1,n+1):
            if i%m==0:
                d.append(i)
            else:
                nd.append(i)
        return sum(nd)-sum(d)
