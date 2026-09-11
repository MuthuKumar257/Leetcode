# Last updated: 9/11/2026, 9:36:21 AM
class Solution:
        def removePalindromeSub(self, s):
            return 2 - (s == s[::-1]) - (s == "")