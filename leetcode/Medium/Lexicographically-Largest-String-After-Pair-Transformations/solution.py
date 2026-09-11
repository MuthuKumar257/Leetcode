"""
LeetCode: Lexicographically Largest String After Pair Transformations
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/lexicographically-largest-string-after-pair-transformations/
"""

class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        ans=[]
        for n in nums:
            s=[]
            while n>0:
                p=1<<(n.bit_length()-1)
                power=min(p.bit_length()-1,25)
                s.append(chr(ord('a')+power))
                n-=(1<<power)
            ans.append("".join(s))
        return ans
