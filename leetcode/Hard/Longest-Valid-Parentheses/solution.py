"""
LeetCode: Longest Valid Parentheses
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/longest-valid-parentheses/
"""

opening = closing = 0
        for ch in reversed(s):
            if ch == "(":
                opening += 1
            else:
                closing += 1

            if opening == closing:
                answer = max(answer, 2 * opening)
            elif opening > closing:
                opening = closing = 0

        return answer
