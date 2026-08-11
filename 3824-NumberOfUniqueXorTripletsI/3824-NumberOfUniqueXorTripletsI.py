# Last updated: 8/11/2026, 6:32:21 PM
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        return n if (n:=len(nums))<3 else 1<<n.bit_length()