# Last updated: 8/11/2026, 6:42:31 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_sum = sum(nums[:k])
        max_sum = w_sum

        for i in range(k,len(nums)):
            w_sum += nums[i] - nums[i-k]
            max_sum  = max(max_sum,w_sum)
        return max_sum/k