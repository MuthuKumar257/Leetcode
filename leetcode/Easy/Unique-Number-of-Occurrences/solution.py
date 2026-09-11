"""
LeetCode: Unique Number of Occurrences
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/unique-number-of-occurrences/
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a=[]
        while len(arr)>0:
            a.append(arr.count(arr[0]))
            arr=list(filter(lambda x: x != arr[0], arr))
            
        return len(a)==len(set(a))
