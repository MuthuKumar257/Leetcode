# Last updated: 8/27/2026, 1:34:19 PM
class Solution:
    def isPalindromic(self, s: str) -> bool:
        b="".join(format(ord(c),'08b') for c in s)
        return b==b[::-1]