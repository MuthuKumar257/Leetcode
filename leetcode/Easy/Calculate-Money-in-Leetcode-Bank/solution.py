"""
LeetCode: Calculate Money in Leetcode Bank
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/calculate-money-in-leetcode-bank/
"""

class Solution(object):
    def totalMoney(self, n):
        weeks, days = divmod(n, 7)
        amount = (weeks*(weeks-1)//2)*7 + weeks*28 + (days*(days+1)//2) + weeks*days
        return amount
