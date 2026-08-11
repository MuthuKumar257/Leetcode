# Last updated: 8/11/2026, 6:30:06 PM
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        z,o=0,0
        r=0
        for i in s:
            if i=='0':
                z+=1
            else:
                o+=1

            if abs(z-o)<=1:
                r+=1
        return r