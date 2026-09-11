# Last updated: 9/11/2026, 9:27:50 AM
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=[0]
        r=[]
        for i in range(len(nums)-1):
            l.append(l[i]+nums[i])
            r.append(sum(nums[i+1:]))
        r.append(0)
        return [abs(l1-r1) for l1,r1 in zip(l,r)]