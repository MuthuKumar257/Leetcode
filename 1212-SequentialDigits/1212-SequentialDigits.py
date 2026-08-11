# Last updated: 8/11/2026, 6:39:48 PM
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        s = "123456789"
        l = str(low)
        h = str(high)

        for length in range(len(l), len(h) + 1):
            for start in range(0, 10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    ans.append(num)

        return ans