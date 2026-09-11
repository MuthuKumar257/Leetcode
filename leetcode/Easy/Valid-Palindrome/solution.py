"""
LeetCode: Valid Palindrome
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/valid-palindrome/
"""

class Solution(object):
    def isPalindrome(self, s):
        s1=""
        for i in s:
            if i.isalnum():
                s1+=i
        return s1.lower() == s1[::-1].lower()
