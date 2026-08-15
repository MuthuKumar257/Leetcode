# Last updated: 8/15/2026, 7:52:50 PM
1class Solution:
2    def longestSubsequence(self, nums: List[int]) -> int:
3        return 0 if all(x==0 for x in nums) else len(nums)-(reduce(xor, nums, 0)==0)