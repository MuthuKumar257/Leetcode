"""
LeetCode: Check Divisibility by Digit Sum and Product
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
"""

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_digit = 0
        product_digit = 1
        num = n


        while num > 0:
            sum_digit += num % 10
            product_digit *= num % 10
            num //= 10


        return n % (sum_digit + product_digit) == 0
