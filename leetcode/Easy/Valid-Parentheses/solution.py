"""
LeetCode: Valid Parentheses
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/valid-parentheses/
"""

elif c == '[':
                stack[head] = ']'
                head += 1
            else:
                if head == 0:
                    return False

                head -= 1

                if stack[head] != c:
                    return False

        return head == 0
