"""
LeetCode: Brace Expansion II
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/brace-expansion-ii/
"""

cur = self.product(cur, nxt)
            elif self.expr[self.i] == ',':
                res |= cur
                cur = {""}
                self.i += 1
            else:
                nxt = {self.expr[self.i]}
                self.i += 1
                cur = self.product(cur, nxt)
        res |= cur
        return res
    def product(self, a, b):
        return {x + y for x in a for y in b}
