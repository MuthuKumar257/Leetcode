"""
LeetCode: X of a Kind in a Deck of Cards
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
"""

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        from math import gcd
        from functools import reduce
        deckCnt = []
        for card in set(deck):
            deckCnt.append(deck.count(card))
        return reduce(gcd,deckCnt) > 1
