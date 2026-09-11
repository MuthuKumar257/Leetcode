# Last updated: 9/11/2026, 9:21:51 AM
class Solution:
    def countCommas(self, n: int) -> int:
        return max(0, n+1-1000)+max(0, n+1-int(1e6))+max(0, n+1-int(1e9))+max(0, n+1-int(1e12))+max(0, n+1-int(1e15))