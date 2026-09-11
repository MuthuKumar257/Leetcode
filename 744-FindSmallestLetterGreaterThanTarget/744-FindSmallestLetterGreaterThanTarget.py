# Last updated: 9/11/2026, 9:42:00 AM
class Solution:
    def nextGreatestLetter(self, L: List[str], target: str) -> str:
        return L[i] if (i:=bisect_right(L, target))<len(L) else L[0]
        