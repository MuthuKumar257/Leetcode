"""
LeetCode: Reorder Data in Log Files
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/reorder-data-in-log-files/
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def customSort(log):
            idx = log.index(' ') + 1
            if log[idx].isalpha():
                return (0, log[idx:], log[:idx])
            return (1,)

        return sorted(logs, key=customSort)
