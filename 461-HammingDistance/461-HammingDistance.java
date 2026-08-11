// Last updated: 8/11/2026, 6:44:06 PM
public class Solution {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);
    }
}