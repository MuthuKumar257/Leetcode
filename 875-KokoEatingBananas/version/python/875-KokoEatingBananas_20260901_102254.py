# Last updated: 9/1/2026, 10:22:54 AM
1class Solution:
2    def singleNonDuplicate(self, nums: list[int]) -> int:
3        start = 0
4        end = len(nums) - 1
5        n = len(nums)
6
7        if n == 1:
8            return nums[0]
9
10        while start <= end:
11            mid = start + (end - start) // 2
12
13            if mid == 0 and nums[0] != nums[1]:
14                return nums[mid]
15            if mid == n - 1 and nums[n - 1] != nums[n - 2]:
16                return nums[mid]
17            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
18                return nums[mid]
19
20            if mid % 2 == 0:
21                if nums[mid - 1] == nums[mid]:
22                    end = mid - 1
23                else:
24                    start = mid + 1
25            else:
26                if nums[mid - 1] == nums[mid]:
27                    start = mid + 1
28                else:
29                    end = mid - 1
30
31        return -1