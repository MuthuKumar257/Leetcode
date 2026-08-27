# Last updated: 8/27/2026, 1:34:16 PM
class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        x,y=target
        ind=-1
        dis=float('inf')
        for i,(a,b,c)in enumerate(drones):
            dis1=abs(a-x)+abs(b-y)
            if dis1<=c:
                if dis1<dis:
                    dis=dis1
                    ind=i
        return ind