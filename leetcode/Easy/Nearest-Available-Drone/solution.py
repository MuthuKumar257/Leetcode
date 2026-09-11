"""
LeetCode: Nearest Available Drone
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/nearest-available-drone/
"""

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
