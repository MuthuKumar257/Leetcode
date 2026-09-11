"""
LeetCode: Find Greatest Common Divisor of Array
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/find-greatest-common-divisor-of-array/
"""

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        smallest = min(nums)
        largest = max(nums)

        return math.gcd(smallest, largest)
