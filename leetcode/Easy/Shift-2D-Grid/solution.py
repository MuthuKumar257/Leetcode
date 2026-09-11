"""
LeetCode: Shift 2D Grid
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/shift-2d-grid/
"""

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flat,m,n = list(chain.from_iterable(grid)), len(grid), len(grid[0])
        return  [(flat[-(k % (m*n)):]+flat)[i*n : (i+1)*n] for i in range(m)]
