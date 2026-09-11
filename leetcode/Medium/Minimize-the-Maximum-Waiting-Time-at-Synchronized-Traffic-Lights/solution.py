"""
LeetCode: Minimize the Maximum Waiting Time at Synchronized Traffic Lights
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/
"""

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
