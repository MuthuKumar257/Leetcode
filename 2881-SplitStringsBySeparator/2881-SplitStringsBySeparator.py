# Last updated: 8/11/2026, 6:34:29 PM
class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        a1=[]
        for i in words:
            a=list(map(str,i.strip(separator).split(separator)))    
            for j in a:
                if j!="":
                    a1.append(j.strip())
        return a1    