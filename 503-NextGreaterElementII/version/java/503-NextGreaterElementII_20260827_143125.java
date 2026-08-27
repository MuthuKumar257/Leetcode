// Last updated: 8/27/2026, 2:31:25 PM
1class Solution {
2        public int[] nextGreaterElements(int[] A) {
3        int n = A.length, res[] = new int[n];
4        Arrays.fill(res, -1);
5        Stack<Integer> stack = new Stack<>();
6        for (int i = 0; i < n * 2; i++) {
7            while (!stack.isEmpty() && A[stack.peek()] < A[i % n])
8                res[stack.pop()] = A[i % n];
9            stack.push(i % n);
10        }
11        return res;
12    }
13}