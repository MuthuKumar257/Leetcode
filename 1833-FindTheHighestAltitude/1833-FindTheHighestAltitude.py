# Last updated: 8/11/2026, 6:36:56 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[0]
        for i in gain:
            a.append(a[len(a)-1]+i)
        return max(a)