# Last updated: 8/11/2026, 6:34:47 PM
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        for i in range(len(s)):
            if s[i] == "L":
                nums[i] -= d
            else:
                nums[i] += d

        nums.sort()

        ans = s = 0 ## s -> sum of previous elements
        for i, n in enumerate(nums):
            ans += i * n - s
            s += n
        return ans % (10**9 + 7)
