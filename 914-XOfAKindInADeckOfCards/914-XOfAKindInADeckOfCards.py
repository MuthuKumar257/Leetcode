# Last updated: 9/11/2026, 9:41:04 AM
class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        from math import gcd
        from functools import reduce
        deckCnt = []
        for card in set(deck):
            deckCnt.append(deck.count(card))
        return reduce(gcd,deckCnt) > 1