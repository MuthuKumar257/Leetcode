"""
LeetCode: Process String with Special Operations I
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/process-string-with-special-operations-i/
"""

class Solution:
    def processStr(self, s: str) -> str:
        a=""
        for i in s:
            if i=='*':
                a=a[:len(a)-1]
            elif i=='#':
                a=a*2
            elif i=='%':
                a=a[::-1]
            else:
                a+=i
           
        return a
