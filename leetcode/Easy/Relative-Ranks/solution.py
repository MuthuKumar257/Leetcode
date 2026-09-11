"""
LeetCode: Relative Ranks
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/relative-ranks/
"""

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        n = len(score)
        ranks = defaultdict(int)

        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        medals.extend(map(str,range(4, n + 1)))

        for idx, val in enumerate(sorted(score,reverse = True)):
            ranks[val] = medals[idx]

        return list(map(lambda s: ranks[s], score))
