"""
LeetCode: String to Integer (atoi)
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/string-to-integer-atoi/
"""

class Solution:
        def myAtoi(self, s: str) -> int:
            length, i, sign, res = len(s), 0, +1, ''
            
            while i < length and s[i] == ' ': i = i + 1
                
            if i < length and s[i] in ('-', '+'): 
                sign, i = -1 if s[i] == '-' else +1, i + 1
                
            while i < length and s[i].isdigit(): 
                res, i = res + s[i], i + 1
            
            return max( -2**31, min( sign * int(res or 0), 2**31 - 1 ) )
