# Last updated: 8/11/2026, 6:35:45 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        return (
            [n for n in nums if n < pivot] +
            [n for n in nums if n == pivot] +
            [n for n in nums if n > pivot]
        )
        