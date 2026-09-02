# Last updated: 9/2/2026, 8:03:55 PM
1class Solution(object):
2    def characterReplacement(self, s, k):
3        max_count = 0
4        left = 0
5        freq = {}
6        
7        for right in range(len(s)):
8            freq[s[right]] = freq.get(s[right], 0) + 1
9            max_count = max(max_count, freq[s[right]])
10            
11            if right - left + 1 - max_count > k:
12                freq[s[left]] -= 1
13                left += 1
14                
15        return len(s) - left