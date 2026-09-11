# Last updated: 9/11/2026, 9:38:10 AM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        a=text.split(" ")
        w=0
        for i in a:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                w+=1
        return w
        