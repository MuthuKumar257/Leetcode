# Last updated: 8/11/2026, 6:44:16 PM

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        missing = []

        for i in range(1,len(nums)+1):
            if i not in set_nums:
                missing.append(i)

        return missing