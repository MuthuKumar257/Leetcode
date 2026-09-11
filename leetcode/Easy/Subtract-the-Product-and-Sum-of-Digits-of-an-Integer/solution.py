"""
LeetCode: Subtract the Product and Sum of Digits of an Integer
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        for i in str(n):
            s+=int(i)
            p*=int(i)
        return p-s
