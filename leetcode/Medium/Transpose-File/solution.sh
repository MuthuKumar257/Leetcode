# LeetCode: Transpose File
# Difficulty: Medium
# Language: Bash
# Problem: https://leetcode.com/problems/transpose-file/

# Read from the file file.txt and print its transposed content to stdout.
awk '
{
    for (i = 1; i <= NF; i++)
        a[i] = a[i] ? a[i] FS $i : $i
}
END {
    for (i = 1; i <= NF; i++)
        print a[i]
}' file.txt
