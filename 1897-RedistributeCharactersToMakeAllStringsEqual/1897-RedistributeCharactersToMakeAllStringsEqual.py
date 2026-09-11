# Last updated: 9/11/2026, 9:31:45 AM
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = {}
        
        for word in words:
            for c in word:
                counts[c] = counts.get(c, 0) + 1
        
        n = len(words)
        for val in counts.values():
            if val % n != 0:
                return False
        
        return True

