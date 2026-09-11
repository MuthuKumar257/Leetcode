# Last updated: 9/11/2026, 9:32:39 AM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0]
        for i in gain:
            a.append(a[len(a)-1]+i)
        return max(a)