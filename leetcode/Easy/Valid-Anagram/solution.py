"""
LeetCode: Valid Anagram
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/valid-anagram/
"""

class Solution(object):
    def isAnagram(self, s, t):
        ana1={}
        ana2={}
        for i in s:
            if i in ana1:
                ana1[i]+=1
            else:
                ana1[i]=1
        
        for i in t:
            if i in ana2:
                ana2[i]+=1
            else:
                ana2[i]=1
        return ana1==ana2
