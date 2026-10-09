"""
LeetCode: Minimum Insertions to Balance a Parentheses String
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
"""

x += 1
            else:
                if i < n - 1 and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1
                if x == 0:
                    ans += 1
            if s[i] == '(':
        while i < n:
        i, n = 0, len(s)
        ans = x = 0
class Solution:
    def minInsertions(self, s: str) -> int:
