# Last updated: 9/11/2026, 9:38:30 AM
class Solution(object):
    def decompressRLElist(self, nums):
        a=[]
        for i in range(0,len(nums),2):
            a1=[nums[i+1]]*nums[i]
            a+=a1
        return a

        