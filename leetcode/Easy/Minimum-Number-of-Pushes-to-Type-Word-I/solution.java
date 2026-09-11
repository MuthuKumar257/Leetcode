/*
 * LeetCode: Minimum Number of Pushes to Type Word I
 * Difficulty: Easy
 * Language: Java
 * Problem: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/
 */

class Solution {
    public int minimumPushes(String word) {
        int ans = 0;
        for(int i = 0; i < word.length(); i++)
            ans += (i / 8) + 1;
        return ans;
    }
}
