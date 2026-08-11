# Last updated: 8/11/2026, 6:37:30 PM
class Solution:
    def restoreString(self, s: str, p: List[int]) -> str:
        return ''.join([v for (_,v) in sorted(zip(p,s))])