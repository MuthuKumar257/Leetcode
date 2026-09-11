"""
LeetCode: Left and Right Sum Differences
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/left-and-right-sum-differences/
"""

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=[0]
        r=[]
        for i in range(len(nums)-1):
            l.append(l[i]+nums[i])
            r.append(sum(nums[i+1:]))
        r.append(0)
        return [abs(l1-r1) for l1,r1 in zip(l,r)]
