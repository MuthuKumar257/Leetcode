# Last updated: 9/9/2026, 10:21:51 AM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        return max(0, n+1-1000)+max(0, n+1-int(1e6))+max(0, n+1-int(1e9))+max(0, n+1-int(1e12))+max(0, n+1-int(1e15))