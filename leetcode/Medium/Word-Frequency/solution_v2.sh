# LeetCode: Word Frequency
# Difficulty: Medium
# Language: Bash
# Problem: https://leetcode.com/problems/word-frequency/

# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s '[:space:]' '\n' | sort | uniq -c | sort -nr | awk '{print $2, $1}'
