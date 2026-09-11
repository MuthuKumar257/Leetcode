// Last updated: 9/11/2026, 9:42:31 AM
class Solution {
    public boolean judgeSquareSum(int c) {
        long j = (long) Math.sqrt(c);
        long i = 0;
        while(i<=j){
            long value = (i*i) + (j*j) ;
            if(value==c) return true;
            else if (value>c) j--;
            else i++;
        }
        return false;
        
    }
}