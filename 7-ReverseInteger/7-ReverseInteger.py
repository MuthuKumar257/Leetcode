# Last updated: 8/11/2026, 6:51:59 PM
class Solution(object):
    def reverse(self, x):
        rev=0
        fla=1
        if x<0:
            x=x*-1
            fla=0
        
        while x!=0:
            a=x%10
            rev=rev*10+a
            x=x//10
        if fla==1 and rev<2147483648:
            return rev
        elif fla==0 and rev<2147483648:
            return -rev  
        else:
            return 0  
        