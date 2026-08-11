# Last updated: 8/11/2026, 6:43:37 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        str1=list(map(str,s.split(" ")))
        j=""
        for i in str1:
            j=j+i[::-1]+" "
        return j.strip()