# Last updated: 9/11/2026, 9:25:45 AM
class Solution:
    def countKeyChanges(self, s: str, ans = 0) -> int:

        for a,b in pairwise(s.lower()):
            ans+= a != b

        return ans