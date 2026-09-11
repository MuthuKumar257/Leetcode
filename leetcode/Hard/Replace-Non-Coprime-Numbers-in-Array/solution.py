"""
LeetCode: Replace Non-Coprime Numbers in Array
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
"""

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g == 1:
                    break
                num = (stack.pop() * num) // g
            stack.append(num)

        return stack
