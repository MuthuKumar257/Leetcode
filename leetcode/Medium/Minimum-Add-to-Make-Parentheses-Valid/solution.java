/*
 * LeetCode: Minimum Add to Make Parentheses Valid
 * Difficulty: Medium
 * Language: Java
 * Problem: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
 */

if (c == '(') {
                open++;
            } else {
                if (open > 0) {
                    open--;
                } else {
                    add++;
                }
            }
        }
        return add + open;
    }
}
