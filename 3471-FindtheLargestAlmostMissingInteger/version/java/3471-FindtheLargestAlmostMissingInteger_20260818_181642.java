// Last updated: 8/18/2026, 6:16:42 PM
1class Solution {
2    public int largestInteger(int[] nums, int k) {
3        HashMap<Integer, Integer> map = new HashMap<>();
4
5        for (int i = 0; i < nums.length; i++) {
6            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
7        }
8
9        if (k == 1) {
10            int ans = -1;
11
12            for (int i = 0; i < nums.length; i++) {
13                if (map.get(nums[i]) == 1 && nums[i] > ans) {
14                    ans = nums[i];
15                }
16            }
17
18            return ans;
19        }
20
21        else if (k == nums.length) {
22            int max = Integer.MIN_VALUE;
23
24            for (int i = 0; i < nums.length; i++) {
25                max = Math.max(nums[i], max);
26            }
27
28            return max;
29        }
30
31        else {
32            int first = nums[0];
33            int last = nums[nums.length - 1];
34
35            boolean first_count = map.get(first) == 1;
36            boolean second_count = map.get(last) == 1;
37
38            if (first_count && second_count)
39                return Math.max(first, last);
40
41            if (first_count)
42                return first;
43
44            if (second_count)
45                return last;
46
47            return -1;
48        }
49    }
50}