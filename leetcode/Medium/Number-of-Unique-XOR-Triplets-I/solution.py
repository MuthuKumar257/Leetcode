"""
LeetCode: Number of Unique XOR Triplets I
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/number-of-unique-xor-triplets-i/
"""

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        return n if (n:=len(nums))<3 else 1<<n.bit_length()
