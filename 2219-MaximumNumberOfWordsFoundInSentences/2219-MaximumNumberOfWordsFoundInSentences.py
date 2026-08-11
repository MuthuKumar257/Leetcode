# Last updated: 8/11/2026, 6:35:55 PM
class Solution(object):
    def mostWordsFound(self, sentences):
        a=[]
        # max1=0
        for i in range(len(sentences)):
            a.append(len(sentences[i].split(" ")))
            # if max1<a[i]:
                # max1=a[i]
        return max(a)
        