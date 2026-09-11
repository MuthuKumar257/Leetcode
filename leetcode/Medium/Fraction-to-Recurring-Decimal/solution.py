"""
LeetCode: Fraction to Recurring Decimal
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/fraction-to-recurring-decimal/
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        num, den = abs(numerator), abs(denominator)
        res.append(str(num // den))
        remainder = num % den
        if remainder == 0:
            return "".join(res)

        res.append(".")
        seen = {}
        while remainder:
            if remainder in seen:
                idx = seen[remainder]
                res.insert(idx, "(")
                res.append(")")
                return "".join(res)
            seen[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // den))
            remainder %= den

        return "".join(res)
