# Last updated: 9/11/2026, 9:22:01 AM
class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        freq = Counter(cntr.values())

        for qty, cnt in freq.items():
            if cnt == 1: break
        else: return -1

        for num, val in cntr.items():
            if val == qty: return num