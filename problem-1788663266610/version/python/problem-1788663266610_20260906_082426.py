# Last updated: 9/6/2026, 8:24:26 AM
1import heapq
2class Solution:
3    def minCost(self, grid: list[list[int]], k: int) -> int:
4        m,n=len(grid),len(grid[0])
5        heap=[(grid[0][0],0,0,-1,0)]
6        seen=set()
7        while heap:
8            cost,r,c,direction,turns=heapq.heappop(heap)
9            if(r,c,direction,turns)in seen:
10                continue
11            seen.add((r,c,direction,turns))
12            if r==m-1 and c==n-1:
13                return cost
14            for d in range(4):
15                dr,dc=[[1,0],[-1,0],[0,1],[0,-1]][d]
16                nr,nc=r+dr,c+dc
17                if 0<=nr<m and 0<=nc<n:
18                    new_turn=turns
19                    if direction !=-1 and direction!=d:
20                        new_turn+=1
21                    if new_turn<=k:
22                        heapq.heappush(heap,(cost+grid[nr][nc],nr,nc,d,new_turn))
23        return -1