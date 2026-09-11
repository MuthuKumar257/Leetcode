# Last updated: 9/11/2026, 9:20:34 AM
class Solution:
    def isPalindromic(self, s: str) -> bool:
        b="".join(format(ord(c),'08b') for c in s)
        return b==b[::-1]