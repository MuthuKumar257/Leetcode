"""
LeetCode: Redistribute Characters to Make All Strings Equal
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
"""

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = {}
        
        for word in words:
            for c in word:
                counts[c] = counts.get(c, 0) + 1
        
        n = len(words)
        for val in counts.values():
            if val % n != 0:
                return False
        
        return True
