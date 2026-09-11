# Last updated: 9/11/2026, 9:41:28 AM
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def remove_characters(s):
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack

        return remove_characters(s) == remove_characters(t)