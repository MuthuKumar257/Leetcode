# Last updated: 9/6/2026, 8:32:26 AM
1class Solution:
2    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:        
3        left, prod, count = 0, 1, 0
4                
5        for right in range(len(nums)):
6            prod *= nums[right]            
7            
8            while prod >= k and left <= right:                    
9                prod /= nums[left]
10                left += 1                        
11            count += right - left + 1                
12        return count