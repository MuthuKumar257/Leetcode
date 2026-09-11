# Last updated: 9/11/2026, 9:23:25 AM
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