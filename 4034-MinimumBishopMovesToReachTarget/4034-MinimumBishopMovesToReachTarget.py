# Last updated: 9/11/2026, 9:20:19 AM
class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        sr,sc=source
        tr,tc=target
        if source==target or abs(sr-tr)==abs(sc-tc):
            return 1
        if (sr+sc)%2!=(tr+tc)%2:
            return -1
        return 2