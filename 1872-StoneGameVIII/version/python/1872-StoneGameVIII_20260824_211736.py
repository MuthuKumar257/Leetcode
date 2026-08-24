# Last updated: 8/24/2026, 9:17:36 PM
1class Solution:
2    def stoneGameVIII(self, stones: List[int]) -> int:
3        p=list(accumulate(stones))[::-1]
4        dp=p[0]
5        for s in p[1:-1:]:
6            dp=max(dp, s-dp)
7        return dp