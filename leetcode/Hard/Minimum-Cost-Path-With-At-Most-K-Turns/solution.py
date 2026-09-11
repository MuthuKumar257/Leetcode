"""
LeetCode: Minimum Cost Path With At Most K Turns
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/minimum-cost-path-with-at-most-k-turns/
"""

import heapq
class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        heap=[(grid[0][0],0,0,-1,0)]
        seen=set()
        while heap:
            cost,r,c,direction,turns=heapq.heappop(heap)
            if(r,c,direction,turns)in seen:
                continue
            seen.add((r,c,direction,turns))
            if r==m-1 and c==n-1:
                return cost
            for d in range(4):
                dr,dc=[[1,0],[-1,0],[0,1],[0,-1]][d]
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n:
                    new_turn=turns
                    if direction !=-1 and direction!=d:
                        new_turn+=1
                    if new_turn<=k:
                        heapq.heappush(heap,(cost+grid[nr][nc],nr,nc,d,new_turn))
        return -1
