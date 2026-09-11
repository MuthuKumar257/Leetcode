"""
LeetCode: Partition Array According to Given Pivot
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/partition-array-according-to-given-pivot/
"""

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        return (
            [n for n in nums if n < pivot] +
            [n for n in nums if n == pivot] +
            [n for n in nums if n > pivot]
        )
