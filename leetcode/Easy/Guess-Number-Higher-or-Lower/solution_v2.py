"""
LeetCode: Guess Number Higher or Lower
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/guess-number-higher-or-lower/
"""

# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1
