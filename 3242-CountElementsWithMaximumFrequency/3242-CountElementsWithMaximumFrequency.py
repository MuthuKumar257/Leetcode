# Last updated: 8/11/2026, 6:34:04 PM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return (Freq:=Counter(nums)) and (maxF:=max(Freq.values())) and sum(f==maxF for f in Freq.values())*maxF
        