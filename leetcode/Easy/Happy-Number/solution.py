"""
LeetCode: Happy Number
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/happy-number/
"""

class Solution(object):
    def isHappy(self, n):
        hset = set()
        while n != 1:
            if n in hset: return False
            hset.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True
