/*
 * LeetCode: Score of Parentheses
 * Difficulty: Medium
 * Language: Java
 * Problem: https://leetcode.com/problems/score-of-parentheses/
 */

for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '(') {
                ++depth;
            } else {
                --depth;
                if (s.charAt(i - 1) == '(') {
                    score += 1 << depth;
                }
            }
        }
        return score;
    }
}
