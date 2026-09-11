"""
LeetCode: Capitalize the Title
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/capitalize-the-title/
"""

class Solution(object):
    def capitalizeTitle(self, title):
        cstr=""
        for i in title.split(" "):
            if len(i)>2:
                cstr=cstr+i.capitalize() +" "
            else:
                cstr=cstr+i.lower() +" "
        return cstr.strip()
