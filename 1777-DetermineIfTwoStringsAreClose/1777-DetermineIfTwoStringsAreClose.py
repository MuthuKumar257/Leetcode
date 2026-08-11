# Last updated: 8/11/2026, 6:37:10 PM
class Solution:
    
    def closeStrings(self, w1, w2):
        return set(w1) == set(w2) and Counter(Counter(w1).values()) == Counter(Counter(w2).values())