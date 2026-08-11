# Last updated: 8/11/2026, 6:36:00 PM
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq = defaultdict(int)
        for w in words1: freq[w] += 1
        for w in words2: freq[w] -= 1 if freq[w] < 2 else 0
        return sum(freq[w] == 0 for w in freq)