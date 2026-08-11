// Last updated: 8/11/2026, 6:43:58 PM
class Solution {
    public int findComplement(int num) {
        int ans=0,index=0;
        while(num>0){
            if((num&1)==0)ans+=(int)Math.pow(2,index);
            num>>=1;
            index++;
        }
        return ans;
    }
}