# Last updated: 8/11/2026, 6:51:53 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        return str(x)==str(x)[::-1]
        