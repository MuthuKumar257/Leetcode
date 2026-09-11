# Last updated: 9/11/2026, 9:33:43 AM
class Solution:
    def restoreString(self, s: str, p: List[int]) -> str:
        return ''.join([v for (_,v) in sorted(zip(p,s))])