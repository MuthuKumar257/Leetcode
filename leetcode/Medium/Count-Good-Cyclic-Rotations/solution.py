"""
LeetCode: Count Good Cyclic Rotations
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/count-good-cyclic-rotations/
"""

class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n=len(nums)
        half=n//2
        t=sum(nums)
        arr=nums+nums
        ws=sum(arr[:half])
        ans=0
        for i in range(n):
            if 2*ws>t:
                ans+=1
            ws+=arr[i+half]-arr[i]
        return ans
