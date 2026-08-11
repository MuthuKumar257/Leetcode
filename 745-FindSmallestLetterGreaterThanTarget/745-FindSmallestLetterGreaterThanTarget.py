# Last updated: 8/11/2026, 6:41:51 PM
class Solution:
    def nextGreatestLetter(self, L: List[str], target: str) -> str:
        return L[i] if (i:=bisect_right(L, target))<len(L) else L[0]
        