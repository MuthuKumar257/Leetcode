# Last updated: 8/11/2026, 6:49:45 PM
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrack(prev, curr: list):
            if len(curr) == k:
                res.append(curr[:])
                return

            for x in range(prev + 1, n + 1):
                curr.append(x)
                backtrack(x, curr)
                curr.pop()
            return

        backtrack(0, [])
        return res