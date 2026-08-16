# Last updated: 8/16/2026, 8:35:34 AM
1class Solution:
2    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
3        lat={}
4        for i,j in requests:
5            lat[j]=max(lat.get(j,0),i)
6        req=list(lat.items())
7        m=len(req)
8        flo=[x[0] for x in req]
9        arr=[x[1] for x in req]
10        INF=float('inf')
11        dp=[[INF]*m for _ in range(1<<m)]
12        for i in range(m):
13            t=abs(start-flo[i])
14            dp[1<<i][i]=max(t,arr[i])
15        for mask in range(1<<m):
16            for j in range(m):
17                if not mask&(1<<j):
18                    continue
19                ct=dp[mask][j]
20                for k in range(m):
21                    if mask&(1<<k):
22                        continue
23                    t=abs(flo[j]-flo[k])
24                    reach=ct+t
25                    nt=max(reach,arr[k])
26                    nm=mask|(1<<k)
27                    dp[nm][k]=min(dp[nm][k],nt)
28        full=(1<<m)-1
29        return min(dp[full])