# Last updated: 9/11/2026, 9:26:45 AM
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        map = {ch: 0 for ch in vowels}
        for c in s:
            if c in vowels:
                map[c] += 1

        sortedVowel = "AEIOUaeiou"
        ans = ""
        j = 0
        for c in s:
            if c not in vowels:
                ans+=(c)
            else:
                while map[sortedVowel[j]] == 0:
                    j += 1
                ans+=(sortedVowel[j])
                map[sortedVowel[j]] -= 1

        return ans