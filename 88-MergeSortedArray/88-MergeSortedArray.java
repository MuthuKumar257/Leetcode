// Last updated: 8/11/2026, 6:49:30 PM
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int a = m - 1;         // pointer: end of nums1's valid elements
        int b = n - 1;         // pointer: end of nums2
        int z = m + n - 1;     // pointer: current write position (back of nums1)

        // fill from the back: always place the larger element
        while (a >= 0 && b >= 0) {
            if (nums1[a] >= nums2[b]) {
                nums1[z] = nums1[a];
                a--;
            } else {
                nums1[z] = nums2[b];
                b--;
            }
            z--;
        }

        // copy any remaining elements from nums2
        // (remaining nums1 elements are already in place)
        while (b >= 0) {
            nums1[z] = nums2[b];
            b--;
            z--;
        }
    }
}