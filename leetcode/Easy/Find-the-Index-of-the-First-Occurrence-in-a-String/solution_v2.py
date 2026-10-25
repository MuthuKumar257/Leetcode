"""
LeetCode: Find the Index of the First Occurrence in a String
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""

class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1
