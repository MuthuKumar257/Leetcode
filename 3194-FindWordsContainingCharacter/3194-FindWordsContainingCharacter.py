# Last updated: 8/11/2026, 6:34:13 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        a=[]
        for i in  range(len(words)):
            if x in words[i]:
                a.append(i)
        return a