"""
LeetCode: Convert the Temperature
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/convert-the-temperature/
"""

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        a=[]
        k=celsius+273.15
        f=celsius*1.80+32.00
        return [k,f]
