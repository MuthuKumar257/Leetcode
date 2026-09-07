# Last updated: 9/7/2026, 2:43:47 PM
1class Solution:
2    def distinctSubseqII(self, s: str) -> int:
3        MOD = 1000000007
4        
5        dp = 1
6        last = [0] * 26
7        
8        for ch in s:
9            index = ord(ch) - ord('a')
10            
11            old_dp = dp
12            
13            dp = (2 * dp - last[index] + MOD) % MOD
14            
15            last[index] = old_dp
16        
17        return (dp - 1 + MOD) % MOD