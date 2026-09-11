"""
LeetCode: Reverse Words in a String
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/reverse-words-in-a-string/
"""

class Solution(object):
    def reverseWords(self, s):
        a=list(s.split())
        a=a[::-1]
        return " ".join(a)
