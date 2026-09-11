# Last updated: 9/11/2026, 9:20:22 AM
class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            if s[i]==s[(i+1)%n]:
                ans+=1
        if k==ans-1:
            return ans
        if k==ans:
            return n-ans
        return 0