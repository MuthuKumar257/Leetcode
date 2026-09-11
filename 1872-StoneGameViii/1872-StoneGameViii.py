# Last updated: 9/11/2026, 9:31:48 AM
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        p=list(accumulate(stones))[::-1]
        dp=p[0]
        for s in p[1:-1:]:
            dp=max(dp, s-dp)
        return dp