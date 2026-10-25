/*
 * LeetCode: Remove Outermost Parentheses
 * Difficulty: Easy
 * Language: Java
 * Problem: https://leetcode.com/problems/remove-outermost-parentheses/
 */

class Solution {
    public String removeOuterParentheses(String s) {
        StringBuilder ans = new StringBuilder();
        int count = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                if (count > 0)
                    ans.append(c);
                count++;
            } else {
                count--;
                if (count > 0)
                    ans.append(c);
            }
        }

        return ans.toString();
    }
}
