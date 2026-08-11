# Last updated: 8/11/2026, 6:45:25 PM
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()

        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))