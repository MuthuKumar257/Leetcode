"""
LeetCode: Find Smallest Letter Greater Than Target
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"""

class Solution:
    def nextGreatestLetter(self, L: List[str], target: str) -> str:
        return L[i] if (i:=bisect_right(L, target))<len(L) else L[0]
