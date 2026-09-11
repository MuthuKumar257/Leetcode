# Last updated: 9/11/2026, 9:39:30 AM
class Solution:
    def minScoreTriangulation(self, v: List[int]) -> int:
        return (f:=cache(lambda i,j:j-i>1 and min(f(i,k)+v[i]*v[k]*v[j]+f(k,j) for k in range(i+1,j))))(0,len(v)-1)