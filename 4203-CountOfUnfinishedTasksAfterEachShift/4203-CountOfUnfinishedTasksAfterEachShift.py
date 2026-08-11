# Last updated: 8/11/2026, 6:30:50 PM
class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n=len(tasks)
        p=[]
        s=0
        ans=[]
        tem=0
        for i in tasks:
            s+=i
            p.append(s)
        
        for t in shifts:
            
                if tem+t>=s:
                    ans.append(0)
                    tem=0
                else:
                    tem+=t
                    d=bisect_right(p,tem)
                    ans.append(n-d)

            

        return ans