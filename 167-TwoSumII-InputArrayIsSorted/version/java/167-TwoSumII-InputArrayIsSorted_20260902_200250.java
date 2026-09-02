// Last updated: 9/2/2026, 8:02:50 PM
1class Solution {
2    public boolean judgeSquareSum(int c) {
3        long j = (long) Math.sqrt(c);
4        long i = 0;
5        while(i<=j){
6            long value = (i*i) + (j*j) ;
7            if(value==c) return true;
8            else if (value>c) j--;
9            else i++;
10        }
11        return false;
12        
13    }
14}