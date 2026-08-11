# Last updated: 8/11/2026, 6:42:27 PM
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))

        duplicate = actual_sum - unique_sum

        missing = n * (n + 1) // 2 - unique_sum

        return [duplicate, missing]