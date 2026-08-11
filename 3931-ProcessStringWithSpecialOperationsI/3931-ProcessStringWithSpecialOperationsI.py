# Last updated: 8/11/2026, 6:31:47 PM
class Solution:
    def processStr(self, s: str) -> str:
        a=""
        for i in s:
            if i=='*':
                a=a[:len(a)-1]
            elif i=='#':
                a=a*2
            elif i=='%':
                a=a[::-1]
            else:
                a+=i
           
        return a