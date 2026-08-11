# Last updated: 8/11/2026, 6:38:30 PM
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a=abs((30*hour)-(5.5*minutes))
        return min(a,360-a)