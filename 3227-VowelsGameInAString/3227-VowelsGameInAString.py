# Last updated: 9/11/2026, 9:25:21 AM
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aeiou" for c in s)
