"""
LeetCode: Check if the Sentence Is Pangram
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
