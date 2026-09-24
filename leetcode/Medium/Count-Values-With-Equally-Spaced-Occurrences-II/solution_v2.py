"""
LeetCode: Count Values With Equally Spaced Occurrences II
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-ii/
"""

from collections import defaultdict
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d=defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)
        ans=0
        for i in d.values():
            if len(i)>=3:
                gap=i[1]-i[0]
                if all(i[j]-i[j-1]==gap for j in range(2,len(i))):
                    ans+=1
        return ans
