# Last updated: 8/11/2026, 6:30:38 PM
class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        freq = Counter(cntr.values())

        for qty, cnt in freq.items():
            if cnt == 1: break
        else: return -1

        for num, val in cntr.items():
            if val == qty: return num