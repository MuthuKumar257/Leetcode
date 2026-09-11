"""
LeetCode: Unique 3-Digit Even Numbers
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/unique-3-digit-even-numbers/
"""

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        f = Counter(digits)

        res = 0
        for n in range(100, 1000, 2):
            i, r = divmod(n, 100)
            j, k = divmod(r, 10)
            res += f[i] > 0 and f[j] > (i == j) and f[k] > (i == k) + (j == k)

        return res
