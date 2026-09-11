"""
LeetCode: Excel Sheet Column Title
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/excel-sheet-column-title/
"""

class Solution:
    
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)
