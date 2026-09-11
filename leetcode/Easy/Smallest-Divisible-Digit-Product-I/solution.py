"""
LeetCode: Smallest Divisible Digit Product I
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/smallest-divisible-digit-product-i/
"""

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def getDigitMultiply(num):
            multiplier = 1

            while multiplier > 0 and num > 0:
                multiplier *= num % 10
                num //= 10

            return multiplier

        for num in range(n, 101):
            if getDigitMultiply(num) % t == 0:
                return num

        return n
