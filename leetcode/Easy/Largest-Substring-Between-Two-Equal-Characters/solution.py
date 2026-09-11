"""
LeetCode: Largest Substring Between Two Equal Characters
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/largest-substring-between-two-equal-characters/
"""

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        current = len(s) - 1
        for i in range(len(s) - 1, 0, -1):
            for j in range(len(s) - i):
                if s[j] == s[j + i]:
                    return i - 1
        return -1
