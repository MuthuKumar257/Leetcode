"""
LeetCode: Palindromic Path Queries in a Tree
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/palindromic-path-queries-in-a-tree/
"""

path_mask = (
                    fenwick_prefix(tin[u])
                    ^ fenwick_prefix(tin[v])
                    ^ char_mask(labels[w])
                )

                # palindrome condition: ≤ 1 bit set
                answers.append(
                    path_mask == 0 or (path_mask & (path_mask - 1)) == 0
                )

        return answers
