"""
LeetCode: Split Strings by Separator
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/split-strings-by-separator/
"""

class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        a1=[]
        for i in words:
            a=list(map(str,i.strip(separator).split(separator)))    
            for j in a:
                if j!="":
                    a1.append(j.strip())
        return a1
