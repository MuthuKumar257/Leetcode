"""
LeetCode: Valid Subarrays With Matching Sum Digits I
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/
"""

class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        c=0
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                if s%10!=x:
                    continue
                f=s
                while f>=10:
                    f=f//10
                if f==x:
                    c+=1
        return c
