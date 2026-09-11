"""
LeetCode: Minimum Score Triangulation of Polygon
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
"""

class Solution:
    def minScoreTriangulation(self, v: List[int]) -> int:
        return (f:=cache(lambda i,j:j-i>1 and min(f(i,k)+v[i]*v[k]*v[j]+f(k,j) for k in range(i+1,j))))(0,len(v)-1)
