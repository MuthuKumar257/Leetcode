# Last updated: 8/11/2026, 6:50:53 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r=-1
        for i in nums:
            if i==target:
                return nums.index(i)
        return r