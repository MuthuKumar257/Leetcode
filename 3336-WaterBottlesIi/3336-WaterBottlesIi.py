# Last updated: 8/11/2026, 6:33:30 PM
class Solution:
    def maxBottlesDrunk(self, n: int, e: int) -> int:
        o=0
        while n>=e:
             o+=e
             n-=e-1
             e+=1
        return o+n