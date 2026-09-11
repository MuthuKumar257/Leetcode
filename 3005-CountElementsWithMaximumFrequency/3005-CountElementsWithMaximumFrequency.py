# Last updated: 9/11/2026, 9:26:14 AM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return (Freq:=Counter(nums)) and (maxF:=max(Freq.values())) and sum(f==maxF for f in Freq.values())*maxF
        