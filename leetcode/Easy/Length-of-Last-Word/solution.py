"""
LeetCode: Length of Last Word
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/length-of-last-word/
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        strlst=list(map(str,s.strip().split(" ")))
        return len(strlst[-1])
