# Last updated: 8/11/2026, 6:42:14 PM
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        for i in range(len(operations)):
            if operations[i]=='C':
                del a[len(a)-1]
            elif operations[i]=='D':
                a.append(a[len(a)-1]*2)
            elif operations[i]=='+':
                a.append(a[len(a)-1]+a[len(a)-2])
            else:
                a.append(int(operations[i]))
        return sum(a)