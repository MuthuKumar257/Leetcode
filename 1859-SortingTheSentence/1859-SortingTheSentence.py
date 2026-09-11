# Last updated: 9/11/2026, 9:31:53 AM
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