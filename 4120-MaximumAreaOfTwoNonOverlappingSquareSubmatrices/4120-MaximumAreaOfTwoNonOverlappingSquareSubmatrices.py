# Last updated: 8/11/2026, 6:31:08 PM
class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        p=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                p[i+1][j+1]=(mat[i][j]+p[i][j+1]+p[i+1][j]-p[i][j])
        
        def check(k):
            mr=m
            mc=n
            maxr=-1
            maxc=-1
            for i in range(m-k+1):
                for j in range(n-k+1):
                    s=(p[i+k][j+k]-p[i][j+k]-p[i+k][j]+p[i][j])
                    if s==k*k:
                        mr=min(mr,i)
                        maxr=max(maxr,i)
                        mc=min(mc,j)
                        maxc=max(maxc,j)
            return maxr-mr>=k or maxc-mc>=k
        l,h,res=0,min(m,n),0
        while l<=h:
            k=(l+h)//2
            if check(k):
                res=k
                l=k+1
            else:
                h=k-1
        return res*res