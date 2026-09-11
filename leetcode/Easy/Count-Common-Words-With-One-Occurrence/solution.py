"""
LeetCode: Count Common Words With One Occurrence
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/count-common-words-with-one-occurrence/
"""

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq = defaultdict(int)
        for w in words1: freq[w] += 1
        for w in words2: freq[w] -= 1 if freq[w] < 2 else 0
        return sum(freq[w] == 0 for w in freq)
