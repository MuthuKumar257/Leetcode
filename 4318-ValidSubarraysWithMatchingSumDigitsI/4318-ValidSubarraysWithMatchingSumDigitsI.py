# Last updated: 8/11/2026, 6:30:26 PM
class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        c=0
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                if s%10!=x:
                    continue
                f=s
                while f>=10:
                    f=f//10
                if f==x:
                    c+=1
        return c