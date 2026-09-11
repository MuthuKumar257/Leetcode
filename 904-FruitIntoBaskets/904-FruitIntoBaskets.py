# Last updated: 9/11/2026, 9:41:10 AM
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