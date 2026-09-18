"""
LeetCode: Maximum Number of Non-Overlapping Substrings
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
"""

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        counts = Counter(s)
        first = {c: s.find(c) for c in counts}
        last = {c: s.rfind(c) for c in counts}

        res = []
        queue = deque()

        for c in counts:
            queue.appendleft([first[c], last[c], counts[c]])

            left = inf
            right = -inf
