"""
LeetCode: Longest Palindromic Substring
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/longest-palindromic-substring/
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        t=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp=s[i:j+1]
                if temp==temp[::-1] and len(temp)>len(t):
                    t=temp
                    
        return t
