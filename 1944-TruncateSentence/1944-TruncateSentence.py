# Last updated: 8/11/2026, 6:36:47 PM
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])