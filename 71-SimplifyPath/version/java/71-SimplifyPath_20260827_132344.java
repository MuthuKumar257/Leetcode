// Last updated: 8/27/2026, 1:23:44 PM
1class StockSpanner {
2
3    Stack<int[]> stack = new Stack<>();
4    public int next(int price) {
5        int res = 1;
6        while (!stack.isEmpty() && stack.peek()[0] <= price)
7            res += stack.pop()[1];
8        stack.push(new int[]{price, res});
9        return res;
10    }
11}
12
13/**
14 * Your StockSpanner object will be instantiated and called as such:
15 * StockSpanner obj = new StockSpanner();
16 * int param_1 = obj.next(price);
17 */