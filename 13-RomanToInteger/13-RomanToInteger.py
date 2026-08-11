# Last updated: 8/11/2026, 6:51:42 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s1 = 0
        for i in range(len(s)):
            if i + 1 < len(s) and a[s[i]] < a[s[i+1]]:
                s1 -= a[s[i]]  
            else:
                s1 += a[s[i]]  
        return s1
