# Last updated: 8/11/2026, 6:50:03 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p=0
        r=[]
        for i in digits:
            p=p*10+i
        p+=1
        while p>0:
            r.append(p%10)
            p=p//10
        return r[::-1]