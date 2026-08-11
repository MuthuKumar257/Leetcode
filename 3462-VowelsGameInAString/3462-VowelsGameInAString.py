# Last updated: 8/11/2026, 6:33:21 PM
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aeiou" for c in s)
