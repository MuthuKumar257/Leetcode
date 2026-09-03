# Last updated: 9/3/2026, 9:00:57 AM
1class Solution:
2    def uniformArray(self, nums1: list[int]) -> bool:
3        return min(nums1)%2==1 or sum(x&1 for x in nums1)==0