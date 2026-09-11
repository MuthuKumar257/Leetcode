"""
LeetCode: Maximum Number of Distinct Elements After Operations
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/
"""

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 0
        prev = -(1 << 30)
        for a in nums:
            low = a - k
            high = a + k
            x = prev + 1
            if x < low:
                x = low
            if x <= high:
                count += 1
                prev = x
        return count
