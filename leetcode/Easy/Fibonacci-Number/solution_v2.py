"""
LeetCode: Fibonacci Number
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/fibonacci-number/
"""

class Solution:
    def fib(self, n: int) -> int:
        n1,n2=-1,1
        for i in range(n+1):
            t=n1
            n1=n2
            n2=t+n2
        return n2
