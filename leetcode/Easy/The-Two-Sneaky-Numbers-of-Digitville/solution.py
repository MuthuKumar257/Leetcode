"""
LeetCode: The Two Sneaky Numbers of Digitville
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
"""

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        visited = set()

        result = []
        for num in nums:
            if(num not in visited):
                visited.add(num)
            else:
                result.append(num)

        return result
