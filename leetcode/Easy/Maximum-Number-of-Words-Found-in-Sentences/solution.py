"""
LeetCode: Maximum Number of Words Found in Sentences
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
"""

class Solution(object):
    def mostWordsFound(self, sentences):
        a=[]
        # max1=0
        for i in range(len(sentences)):
            a.append(len(sentences[i].split(" ")))
            # if max1<a[i]:
                # max1=a[i]
        return max(a)
