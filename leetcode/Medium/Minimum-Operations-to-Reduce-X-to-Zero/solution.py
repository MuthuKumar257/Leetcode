"""
LeetCode: Minimum Operations to Reduce X to Zero
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
"""

s = i = 0
        
        for j, num in enumerate(A):
            s += num
            while s > k:
                s -= A[i]
                i += 1  
            if s == k:
                best = max(best, j - i + 1)

        return -1 if best < 0 else len(A) - best
