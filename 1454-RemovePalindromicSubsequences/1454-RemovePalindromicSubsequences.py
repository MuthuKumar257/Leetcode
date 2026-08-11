# Last updated: 8/11/2026, 6:38:20 PM
class Solution:
        def removePalindromeSub(self, s):
            return 2 - (s == s[::-1]) - (s == "")