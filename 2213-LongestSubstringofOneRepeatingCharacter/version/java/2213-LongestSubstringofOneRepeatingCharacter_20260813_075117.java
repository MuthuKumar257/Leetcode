// Last updated: 8/13/2026, 7:51:17 AM
1class Solution {
2    int[] pre, suf, best;
3    char[] s;
4
5    public int[] longestRepeating(String str, String q, int[] idx) {
6        s = str.toCharArray();
7        int n = s.length;
8        pre = new int[4*n];
9        suf = new int[4*n];
10        best = new int[4*n];
11
12        build(1, 0, n-1);
13
14        int[] ans = new int[idx.length];
15
16        for (int i = 0; i < idx.length; i++) {
17            s[idx[i]] = q.charAt(i);
18            update(1, 0, n-1, idx[i]);
19            ans[i] = best[1];
20        }
21        return ans;
22    }
23
24    void build(int p, int l, int r) {
25        if (l == r) {
26            pre[p] = suf[p] = best[p] = 1;
27            return;
28        }
29        int m = (l+r)/2;
30        build(p*2, l, m);
31        build(p*2+1, m+1, r);
32        merge(p, l, r);
33    }
34
35    void update(int p, int l, int r, int x) {
36        if (l == r) {
37            pre[p] = suf[p] = best[p] = 1;
38            return;
39        }
40
41        int m = (l+r)/2;
42        if (x <= m) update(p*2, l, m, x);
43        else update(p*2+1, m+1, r, x);
44
45        merge(p, l, r);
46    }
47
48    void merge(int p, int l, int r) {
49        int a = p*2, b = p*2+1, m = (l+r)/2;
50
51        pre[p] = pre[a];
52        suf[p] = suf[b];
53        best[p] = Math.max(best[a], best[b]);
54
55        if (s[m] == s[m+1]) {
56            best[p] = Math.max(best[p], suf[a] + pre[b]);
57
58            if (pre[a] == m-l+1)
59                pre[p] += pre[b];
60
61            if (suf[b] == r-m)
62                suf[p] += suf[a];
63        }
64    }
65}