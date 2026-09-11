"""
LeetCode: Maximum Number of Words You Can Type
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/maximum-number-of-words-you-can-type/
"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        a=text.split(" ")
        w=0
        for i in a:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                w+=1
        return w
