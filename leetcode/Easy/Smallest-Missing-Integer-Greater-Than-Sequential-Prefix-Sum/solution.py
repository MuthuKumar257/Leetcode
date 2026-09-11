"""
LeetCode: Smallest Missing Integer Greater Than Sequential Prefix Sum
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
"""

class Solution:
    def missingInteger(self, A: list[int]) -> int:
        n = len(A)
        seen = set(A)
        sum = A[0]

        for i in range(1, n):
            if A[i] == A[i - 1] + 1:
                sum += A[i]
            else:
                break

        while sum in seen:
            sum += 1

        return sum
