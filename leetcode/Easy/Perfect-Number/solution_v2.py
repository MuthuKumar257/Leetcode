"""
LeetCode: Perfect Number
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/perfect-number/
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        dvisum=1
        if num>1:
            for i in range(2,int(sqrt(num))+1):
                if num%i==0:
                    dvisum=dvisum+i+(num//i)
            return dvisum==num
        else:
            return False
