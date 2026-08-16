# Last updated: 8/16/2026, 8:15:26 AM
1class Solution:
2    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
3        maxgr=max(lights)
4        p=0
5        for i in arrivalTime:
6            r=i%period
7            
8            if r<maxgr:
9               wait=0
10            else:
11               wait=period-r
12
13            p=max(p,wait)
14        return p