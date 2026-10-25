"""
LeetCode: Subarrays Distinct Element Sum of Squares I
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
"""

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n, ans=len(nums), 0
        for l in range(n):
            seen, cnt=0, 0
            for x in nums[l:]:
                cnt+=((seen>>x)&1)==0
                seen|=(1<<x)
                ans+=cnt*cnt
        return ans
