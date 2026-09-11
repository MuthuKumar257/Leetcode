// Last updated: 9/11/2026, 9:25:57 AM
class Solution {
    public int minimumPushes(String word) {
        int ans = 0;
        for(int i = 0; i < word.length(); i++)
            ans += (i / 8) + 1;
        return ans;
    }
}