/*
 * LeetCode: Hamming Distance
 * Difficulty: Easy
 * Language: Java
 * Problem: https://leetcode.com/problems/hamming-distance/
 */

public class Solution {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);
    }
}
