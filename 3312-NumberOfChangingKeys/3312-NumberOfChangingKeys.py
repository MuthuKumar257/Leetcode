# Last updated: 8/11/2026, 6:33:36 PM
class Solution:
    def countKeyChanges(self, s: str, ans = 0) -> int:

        for a,b in pairwise(s.lower()):
            ans+= a != b

        return ans