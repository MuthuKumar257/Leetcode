"""
LeetCode: Median of Two Sorted Arrays
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)

        n = len(merged)
        mid = n // 2

        if n % 2 == 1:
            return merged[mid]
        else:
            return (merged[mid - 1] + merged[mid]) / 2
