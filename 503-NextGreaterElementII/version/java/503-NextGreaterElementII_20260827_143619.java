// Last updated: 8/27/2026, 2:36:19 PM
1public class Solution extends VersionControl {
2    public int firstBadVersion(int n) {
3        int l=0,h=n;
4        while(l<=h){
5            int mid = l+(h-l)/2;
6            if(isBadVersion(mid)) h = mid-1;
7            else l = mid+1;
8        }
9        return l;
10    }
11}