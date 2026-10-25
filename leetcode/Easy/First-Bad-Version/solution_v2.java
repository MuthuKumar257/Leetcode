/*
 * LeetCode: First Bad Version
 * Difficulty: Easy
 * Language: Java
 * Problem: https://leetcode.com/problems/first-bad-version/
 */

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
