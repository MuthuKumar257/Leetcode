# Last updated: 9/11/2026, 9:31:10 AM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s=word.find(ch)
        if s>0:
            str1=word[:s+1]
            str2=word[s+1:]
            return str1[::-1]+str2
        return word