# Last updated: 9/11/2026, 9:24:34 AM
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        f = Counter(digits)

        res = 0
        for n in range(100, 1000, 2):
            i, r = divmod(n, 100)
            j, k = divmod(r, 10)
            res += f[i] > 0 and f[j] > (i == j) and f[k] > (i == k) + (j == k)

        return res