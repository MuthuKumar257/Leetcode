// Last updated: 8/11/2026, 6:47:11 PM
import java.util.Arrays;

class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n; // Handles cases where k is larger than the array length
        
        int[] res = new int[n];
        
        // Compute the shifted positions into the result array
        for (int i = 0; i < n; i++) {
            res[(i + k) % n] = nums[i];
        }
        
        // CRITICAL: Copy data back into the original 'nums' array memory
        System.arraycopy(res, 0, nums, 0, n);
    }
}
