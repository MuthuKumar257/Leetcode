# Last updated: 8/11/2026, 6:44:09 PM
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]