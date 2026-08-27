# Last updated: 8/27/2026, 1:34:20 PM
class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        lat={}
        for i,j in requests:
            lat[j]=max(lat.get(j,0),i)
        req=list(lat.items())
        m=len(req)
        flo=[x[0] for x in req]
        arr=[x[1] for x in req]
        INF=float('inf')
        dp=[[INF]*m for _ in range(1<<m)]
        for i in range(m):
            t=abs(start-flo[i])
            dp[1<<i][i]=max(t,arr[i])
        for mask in range(1<<m):
            for j in range(m):
                if not mask&(1<<j):
                    continue
                ct=dp[mask][j]
                for k in range(m):
                    if mask&(1<<k):
                        continue
                    t=abs(flo[j]-flo[k])
                    reach=ct+t
                    nt=max(reach,arr[k])
                    nm=mask|(1<<k)
                    dp[nm][k]=min(dp[nm][k],nt)
        full=(1<<m)-1
        return min(dp[full])