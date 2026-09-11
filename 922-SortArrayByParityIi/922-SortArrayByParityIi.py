# Last updated: 9/11/2026, 9:40:53 AM
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