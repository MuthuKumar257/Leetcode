# Last updated: 8/28/2026, 9:15:50 AM
1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        
4        def search(x):
5            lo, hi = 0, len(nums)           
6            while lo < hi:
7                mid = (lo + hi) // 2
8                if nums[mid] < x:
9                    lo = mid+1
10                else:
11                    hi = mid                    
12            return lo
13        
14        lo = search(target)
15        hi = search(target+1)-1
16        
17        if lo <= hi:
18            return [lo, hi]
19                
20        return [-1, -1]