"""
LeetCode: Next Greater Element I
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/next-greater-element-i/
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = []
        for i in nums1:
            start_index = nums2.index(i)
            found = False
            for j in range(start_index + 1, len(nums2)):
                if nums2[j] > i:
                    a.append(nums2[j])
                    found = True
                    break
            if not found:
                a.append(-1)

        return a
