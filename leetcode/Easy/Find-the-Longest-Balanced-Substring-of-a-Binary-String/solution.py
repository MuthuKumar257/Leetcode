"""
LeetCode: Find the Longest Balanced Substring of a Binary String
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/
"""

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        res = 0
        it = 0
        while it < len(s):
            oCnt ,zCnt = 0 , 0
            while it < len(s) and s[it] == "0"  :
                zCnt += 1
                it += 1
            while it < len(s) and s[it] == "1":
                oCnt += 1
                it += 1
            res = max(res,2*min(oCnt,zCnt))
        return res
