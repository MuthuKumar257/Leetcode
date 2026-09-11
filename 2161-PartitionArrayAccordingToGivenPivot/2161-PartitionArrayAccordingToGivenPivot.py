# Last updated: 9/11/2026, 9:30:22 AM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        return (
            [n for n in nums if n < pivot] +
            [n for n in nums if n == pivot] +
            [n for n in nums if n > pivot]
        )
        