"""
LeetCode: Maximum Score of Non-overlapping Intervals
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/
"""

for j in range(1, 5):
                prevWeight, prevIndices = dp[k][j - 1]
                
            
            k = bisect_left(sortedIntervals, (start,), hi=i)
        for i, (end, start, weight, originalIndex) in enumerate(sortedIntervals):

        dp = [[(0, []) for _ in range(5)] for _ in range(len(intervals) + 1)]

        sortedIntervals.sort(key=lambda x: x[0])
        (intervals)]
        sortedIntervals = [(r, l, weight, i) for i, (l, r, weight) in enumerate
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
class Solution:
                skip = dp[i][j]
                takeWeight = prevWeight - weight
