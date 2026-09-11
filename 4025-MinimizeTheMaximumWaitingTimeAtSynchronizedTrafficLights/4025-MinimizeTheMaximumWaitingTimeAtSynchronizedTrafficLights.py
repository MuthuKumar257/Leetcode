# Last updated: 9/11/2026, 9:20:36 AM
class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        maxgr=max(lights)
        p=0
        for i in arrivalTime:
            r=i%period
            
            if r<maxgr:
               wait=0
            else:
               wait=period-r

            p=max(p,wait)
        return p