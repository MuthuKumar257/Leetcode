"""
LeetCode: Remove Invalid Parentheses
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/remove-invalid-parentheses/
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            i= 0
            ctr = 0
            while i<len(s):
                if s[i]== '(':
                    ctr += 1
                elif s[i] == ")":
                    if ctr == 0:
                        return False
                    ctr -= 1
                
                i +=1
