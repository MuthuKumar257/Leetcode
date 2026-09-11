# Last updated: 9/11/2026, 9:25:41 AM
class Solution:
    def maxBottlesDrunk(self, n: int, e: int) -> int:
        o=0
        while n>=e:
             o+=e
             n-=e-1
             e+=1
        return o+n