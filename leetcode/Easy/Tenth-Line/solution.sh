# LeetCode: Tenth Line
# Difficulty: Easy
# Language: Bash
# Problem: https://leetcode.com/problems/tenth-line/

# Read from the file file.txt and output the tenth line to stdout.
tail -n +10 file.txt | head -n1
