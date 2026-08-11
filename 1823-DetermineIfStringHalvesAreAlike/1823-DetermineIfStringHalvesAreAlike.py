# Last updated: 8/11/2026, 6:37:03 PM
class Solution:

    def halvesAreAlike(self, S: str) -> bool:
        vowels = "aeiouAEIOU"
        mid, ans = len(S) // 2, 0
        for i in range(mid):
            if S[i] in vowels: ans += 1
            if S[mid+i] in vowels: ans -=1
        return ans == 0