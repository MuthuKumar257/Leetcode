"""
LeetCode: Count Values With Equally Spaced Occurrences I
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-i/
"""

from collections import defaultdict 
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        p=defaultdict(list)
        for x,i in enumerate(nums):
            p[i].append(x)
        ans=0
        for i,x in p.items():
            if len(x)==3:
                a,b,c=x
                if b-a==c-b:
                    ans+=1
        return ans
