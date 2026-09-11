"""
LeetCode: Taking Maximum Energy From the Mystic Dungeon
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/
"""

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        last_k = energy[-k:][::-1]
        for idx in range(len(energy) - k - 1, -1, -1):
            last_k.append(last_k[-k] + energy[idx])
        return max(last_k)
