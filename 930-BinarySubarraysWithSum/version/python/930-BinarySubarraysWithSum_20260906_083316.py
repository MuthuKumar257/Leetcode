# Last updated: 9/6/2026, 8:33:16 AM
1class Solution:
2    def maxFrequency(self, nums: List[int], k: int) -> int:
3        n = len(nums)
4        nums.sort()
5        preSum = [0] * (n + 1)
6        for i in range(n):
7            preSum[i + 1] = preSum[i] + nums[i]
8
9        def getSum(left, right):  # left, right inclusive
10            return preSum[right + 1] - preSum[left]
11
12        def count(index): # Count frequency of `nums[index]` if we make other elements equal to `nums[index]`
13            left = 0
14            right = index
15            res = index
16            while left <= right:
17                mid = left + (right - left) // 2
18                s = getSum(mid, index - 1) # get sum of (nums[mid], nums[mid+1]...nums[index-1])
19                if s + k >= (index - mid) * nums[index]: # Found an answer -> Try to find a better answer in the left side
20                    res = mid  # save best answer so far
21                    right = mid - 1
22                else:
23                    left = mid + 1
24            return index - res + 1
25
26        ans = 0
27        for i in range(n):
28            ans = max(ans, count(i))
29        return ans