"""
LeetCode: Minimum Number of Increments on Subarrays to Form a Target Array
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
"""

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = prev = 0
        for x in target:
            if x > prev:
                res += x - prev
            prev = x
        return res
