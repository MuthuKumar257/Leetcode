# Last updated: 9/11/2026, 9:21:21 AM
class Solution:
    def maxDistance(self, moves: str) -> int:
        r=moves.count('R')
        d=moves.count('D')
        t=moves.count('_')
        l=moves.count('L')
        u=moves.count('U')
        return abs(r-l)+abs(u-d)+t