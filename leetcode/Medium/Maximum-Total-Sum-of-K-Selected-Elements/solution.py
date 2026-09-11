"""
LeetCode: Maximum Total Sum of K Selected Elements
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/
"""

class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        r=0
        for i in range(k):
            if mul>0:
                r+=nums[i]*mul
            else:
                r+=nums[i]
            mul-=1
        return r
