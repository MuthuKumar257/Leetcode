# Last updated: 9/11/2026, 9:20:35 AM
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