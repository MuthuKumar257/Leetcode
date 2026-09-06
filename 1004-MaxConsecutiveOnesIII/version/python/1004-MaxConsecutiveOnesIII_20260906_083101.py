# Last updated: 9/6/2026, 8:31:01 AM
1class Solution:
2    def longestOnes(self, nums, k):
3        left, maxLength, zeroCount = 0, 0, 0
4        for right in range(len(nums)):
5            if nums[right] == 0:
6                zeroCount += 1
7            while zeroCount > k:
8                if nums[left] == 0:
9                    zeroCount -= 1
10                left += 1
11            maxLength = max(maxLength, right - left + 1)
12        return maxLength