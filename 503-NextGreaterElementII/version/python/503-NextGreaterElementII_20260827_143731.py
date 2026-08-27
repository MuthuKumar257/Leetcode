# Last updated: 8/27/2026, 2:37:31 PM
1class Solution:
2    def countCompleteSubstrings(self, w: str, k: int) -> int:
3        def calc(s):
4            res = 0
5            v = len(s)
6            for i in range(1, 27):
7                if i * k > v: break
8                l = i * k
9                cnt = Counter(s[:l])
10                freq = Counter(cnt.values())
11                
12                if freq[k] == i: res += 1
13                
14                for idx in range(v - l):
15                    freq[cnt[s[idx]]] -= 1
16                    cnt[s[idx]] -= 1
17                    freq[cnt[s[idx]]] += 1
18
19                    freq[cnt[s[idx+l]]] -= 1
20                    cnt[s[idx+l]] += 1
21                    freq[cnt[s[idx+l]]] += 1
22
23                    if freq[k] == i: res += 1
24            return res
25        
26        idx = 0
27        ans = 0
28        n = len(w)
29        for i in range(1, n):
30            if abs(ord(w[i]) - ord(w[i-1])) > 2:
31                ans += calc(w[idx:i])
32                idx = i
33        ans += calc(w[idx:])
34        return ans