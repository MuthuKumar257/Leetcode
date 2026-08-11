// Last updated: 8/11/2026, 6:51:04 PM
class Solution {
    public int divide(int dividend, int divisor) {
       if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
       return dividend/divisor; 
    }
}