"""
LeetCode: Remove Element
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/remove-element/
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]=51
                k+=1
        nums.sort()
        return len(nums)-k
