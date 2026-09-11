"""
LeetCode: Decompress Run-Length Encoded List
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/decompress-run-length-encoded-list/
"""

class Solution(object):
    def decompressRLElist(self, nums):
        a=[]
        for i in range(0,len(nums),2):
            a1=[nums[i+1]]*nums[i]
            a+=a1
        return a
