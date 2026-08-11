# Last updated: 8/11/2026, 6:30:20 PM
class Solution:
    def maxDistance(self, moves: str) -> int:
        r=moves.count('R')
        d=moves.count('D')
        t=moves.count('_')
        l=moves.count('L')
        u=moves.count('U')
        return abs(r-l)+abs(u-d)+t