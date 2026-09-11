# Last updated: 9/11/2026, 9:32:59 AM
class Solution:
    
    def closeStrings(self, w1, w2):
        return set(w1) == set(w2) and Counter(Counter(w1).values()) == Counter(Counter(w2).values())