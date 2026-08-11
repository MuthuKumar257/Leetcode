# Last updated: 8/11/2026, 6:52:06 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        t=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp=s[i:j+1]
                if temp==temp[::-1] and len(temp)>len(t):
                    t=temp
                    
        return t