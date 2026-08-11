# Last updated: 8/11/2026, 6:33:53 PM
class Solution:
    def minimumPushes(self, word: str) -> int:

        d, m = divmod(len(word), 8)

        return (4*d+m)*(d+1)