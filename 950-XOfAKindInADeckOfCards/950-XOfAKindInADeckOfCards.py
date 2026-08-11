# Last updated: 8/11/2026, 6:41:17 PM
class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        from math import gcd
        from functools import reduce
        deckCnt = []
        for card in set(deck):
            deckCnt.append(deck.count(card))
        return reduce(gcd,deckCnt) > 1