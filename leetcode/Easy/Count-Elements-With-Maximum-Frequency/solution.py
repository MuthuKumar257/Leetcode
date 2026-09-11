"""
LeetCode: Count Elements With Maximum Frequency
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/count-elements-with-maximum-frequency/
"""

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        return (Freq:=Counter(nums)) and (maxF:=max(Freq.values())) and sum(f==maxF for f in Freq.values())*maxF
