"""
LeetCode: Count Rotations With Exactly K Equal Adjacent Pairs
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/
"""

class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            if s[i]==s[(i+1)%n]:
                ans+=1
        if k==ans-1:
            return ans
        if k==ans:
            return n-ans
        return 0
