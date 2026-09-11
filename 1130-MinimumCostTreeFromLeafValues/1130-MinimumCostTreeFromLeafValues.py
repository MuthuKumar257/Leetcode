# Last updated: 9/11/2026, 9:38:42 AM
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        while(len(arr)>1):
            mx = arr[0]*arr[1]
            l = 0
            r = 1
            for i in range(len(arr)-1):
                if arr[i]*arr[i+1]<mx:
                    mx = arr[i]*arr[i+1]
                    l = i
                    r = i+1
            ans+=mx
            #print(l,r,mx)
            if arr[l]>arr[r]:
                del arr[r]
            else:
                del arr[l]
        return ans
		