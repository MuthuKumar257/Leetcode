# Last updated: 8/11/2026, 6:43:46 PM
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        dvisum=1
        if num>1:
            for i in range(2,int(sqrt(num))+1):
                if num%i==0:
                    dvisum=dvisum+i+(num//i)
            return dvisum==num
        else:
            return False