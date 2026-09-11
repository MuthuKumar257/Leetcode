# Last updated: 9/11/2026, 9:32:28 AM
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])