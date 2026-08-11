# Last updated: 8/11/2026, 6:36:33 PM
class Solution:
    def sortSentence(self, s: str) -> str:
        a=s.split()
        
        res=[]
        for j in range(1,len(s)):
            for i in a:
                if int(i[len(i)-1])==j:
                    res.append(i[:len(i)-1])
                    
                    break
        return " ".join(res)