// Last updated: 9/11/2026, 9:44:43 AM
public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int l=0,h=n;
        while(l<=h){
            int mid = l+(h-l)/2;
            if(isBadVersion(mid)) h = mid-1;
            else l = mid+1;
        }
        return l;
    }
}