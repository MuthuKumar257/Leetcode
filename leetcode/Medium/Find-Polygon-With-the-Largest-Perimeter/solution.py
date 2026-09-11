"""
LeetCode: Find Polygon With the Largest Perimeter
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
"""

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        cur = sum(A)
        while A and cur <= A[-1] * 2:
            cur -= A.pop()
        return sum(A) if len(A) > 2 else -1
