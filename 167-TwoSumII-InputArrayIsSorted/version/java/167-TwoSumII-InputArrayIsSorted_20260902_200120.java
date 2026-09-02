// Last updated: 9/2/2026, 8:01:20 PM
1class Solution {
2    public int removeDuplicates(int[] nums) {
3        int j = 1;
4        for (int i = 1; i < nums.length; i++) {
5            if (j == 1 || nums[i] != nums[j - 2]) {
6                nums[j++] = nums[i];
7            }
8        }
9        return j;
10    }
11}