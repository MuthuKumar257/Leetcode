# Last updated: 8/11/2026, 6:44:13 PM
class Solution:
    def fourSumCount(self, A, B, C, D):
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)