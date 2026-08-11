# Last updated: 8/11/2026, 6:39:30 PM
class Solution(object):
    def decompressRLElist(self, nums):
        a=[]
        for i in range(0,len(nums),2):
            a1=[nums[i+1]]*nums[i]
            a+=a1
        return a

        