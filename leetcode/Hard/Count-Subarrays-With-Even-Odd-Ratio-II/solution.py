"""
LeetCode: Count Subarrays With Even Odd Ratio II
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/
"""

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        p=[0]
        s=0
        for i in nums:
            s+=b if i%2==0 else -a
            p.append(s)
        a1=0
        q=[]
        for i in p:
            t=bisect_left(q,i)
            a1+=len(q)-t
            insort(q,i)
        return a1
