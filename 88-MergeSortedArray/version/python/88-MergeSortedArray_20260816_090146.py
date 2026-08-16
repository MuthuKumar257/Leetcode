# Last updated: 8/16/2026, 9:01:46 AM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """ 
6        for i in range(m,m+n):
7            nums1[i]=nums2[i-m]
8        nums1.sort()