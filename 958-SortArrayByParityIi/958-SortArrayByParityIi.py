# Last updated: 8/11/2026, 6:41:06 PM
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums)):
            for j in nums:
                if i%2==0 and j%2==0:
                    r.append(j)
                    nums.remove(j)
                    break
                if i%2!=0 and j%2!=0:
                    r.append(j)
                    nums.remove(j)
                    break
        return r