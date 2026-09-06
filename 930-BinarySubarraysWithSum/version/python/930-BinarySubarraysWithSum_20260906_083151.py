# Last updated: 9/6/2026, 8:31:51 AM
1class Solution:
2    def numSubarraysWithSum(self, A, S):
3        c = collections.Counter({0: 1})
4        psum = res = 0
5        for i in A:
6            psum += i
7            res += c[psum - S]
8            c[psum] += 1
9        return res