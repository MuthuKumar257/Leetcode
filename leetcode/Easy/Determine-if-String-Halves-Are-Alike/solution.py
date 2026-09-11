"""
LeetCode: Determine if String Halves Are Alike
Difficulty: Easy
Language: Python
Problem: https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""

class Solution:

    def halvesAreAlike(self, S: str) -> bool:
        vowels = "aeiouAEIOU"
        mid, ans = len(S) // 2, 0
        for i in range(mid):
            if S[i] in vowels: ans += 1
            if S[mid+i] in vowels: ans -=1
        return ans == 0
