# Last updated: 8/11/2026, 6:51:09 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)