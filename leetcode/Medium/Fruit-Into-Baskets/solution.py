"""
LeetCode: Fruit Into Baskets
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/fruit-into-baskets/
"""

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        l = 0
        ans = 0

        for r in range(len(fruits)):
            d[fruits[r]] = r

            if len(d) > 2:
                k = min(d, key=d.get)
                l = d[k] + 1
                del d[k]

            ans = max(ans, r - l + 1)

        return ans
