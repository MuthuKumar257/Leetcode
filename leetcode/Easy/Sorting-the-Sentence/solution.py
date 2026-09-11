"""
LeetCode: Sorting the Sentence
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/sorting-the-sentence/
"""

class Solution:
    def sortSentence(self, s: str) -> str:
        a=s.split()
        
        res=[]
        for j in range(1,len(s)):
            for i in a:
                if int(i[len(i)-1])==j:
                    res.append(i[:len(i)-1])
                    
                    break
        return " ".join(res)
