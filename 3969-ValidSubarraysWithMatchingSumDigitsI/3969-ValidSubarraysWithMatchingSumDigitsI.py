# Last updated: 9/11/2026, 9:21:33 AM
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