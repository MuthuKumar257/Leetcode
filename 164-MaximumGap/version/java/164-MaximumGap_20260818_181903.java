// Last updated: 8/18/2026, 6:19:03 PM
1class Solution {
2    public int maximumGap(int[] nums) {
3        int min = nums[0], max = nums[0], n = nums.length;
4        for (int x : nums) {
5            min = Math.min(min, x);
6            max = Math.max(max, x);
7        }
8        if (min == max) return 0; // All elements are the same
9        int bucketSize = (int) Math.ceil((double) (max - min) / (n - 1));
10        int[] minBucket = new int[n];
11        int[] maxBucket = new int[n];
12        Arrays.fill(minBucket, Integer.MAX_VALUE);
13        Arrays.fill(maxBucket, Integer.MIN_VALUE);
14        for (int x : nums) {
15            int idx = (x - min) / bucketSize;
16            minBucket[idx] = Math.min(x, minBucket[idx]);
17            maxBucket[idx] = Math.max(x, maxBucket[idx]);
18        }
19        int maxGap = bucketSize; // Maximum gap is always greater or equal to bucketSize
20        int previous = maxBucket[0]; // We always have 0th bucket
21        for (int i = 1; i < n; i++) {
22            if (minBucket[i] == Integer.MAX_VALUE) continue; // Skip empty bucket
23            maxGap = Math.max(maxGap, minBucket[i] - previous);
24            previous = maxBucket[i];
25        }
26        return maxGap;
27    }
28}