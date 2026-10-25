"""
LeetCode: Reverse Words in a String III
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        str1=list(map(str,s.split(" ")))
        j=""
        for i in str1:
            j=j+i[::-1]+" "
        return j.strip()
