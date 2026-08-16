# Last updated: 8/16/2026, 9:08:53 AM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k=0
4        for i in range(len(nums)):
5            if nums[i]==val:
6                nums[i]=51
7                k+=1
8        nums.sort()
9        return len(nums)-k