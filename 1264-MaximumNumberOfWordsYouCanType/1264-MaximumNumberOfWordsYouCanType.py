# Last updated: 8/11/2026, 6:39:14 PM
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
        