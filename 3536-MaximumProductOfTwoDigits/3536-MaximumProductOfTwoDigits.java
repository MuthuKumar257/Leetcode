// Last updated: 9/11/2026, 9:23:43 AM
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