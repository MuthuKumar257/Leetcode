"""
LeetCode: Successful Pairs of Spells and Potions
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
"""

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        potion_count = len(potions)
        result = []
        for spell_power in spells:
            required_strength = math.ceil(success / spell_power)
            if required_strength > potions[-1]:
                result.append(0)
                continue
            index = bisect.bisect_left(potions, required_strength)
            result.append(potion_count - index)
        return result
