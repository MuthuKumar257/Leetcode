# Last updated: 8/11/2026, 6:36:03 PM
class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = i = 0
        while i < len(s): 
            if s[i] == "X": 
                ans += 1
                i += 3
            else: i += 1
        return ans 