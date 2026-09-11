/*
 * LeetCode: Maximum Product of Two Digits
 * Difficulty: Easy
 * Language: Java
 * Problem: https://leetcode.com/problems/maximum-product-of-two-digits/
 */

class Solution {
    public int maxProduct(int n) {
        if(n<=9)return n;
        int max=0,sMax=0;
        while(n>0){
            int currem=n%10;
            if(currem>max){
                sMax=max;
                max=currem;
            }else if(currem>sMax)sMax=currem;
            n/=10;
        }
        return sMax*max;
    }
}
