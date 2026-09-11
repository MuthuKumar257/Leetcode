# Last updated: 9/11/2026, 9:37:16 AM
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a=abs((30*hour)-(5.5*minutes))
        return min(a,360-a)