"""
LeetCode: Fizz Buzz
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/fizz-buzz/
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        r=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                r.append("FizzBuzz")
            elif i%3==0:
                r.append("Fizz")
            elif i%5==0:
                r.append("Buzz")
            else:
                r.append(str(i))
        return r
