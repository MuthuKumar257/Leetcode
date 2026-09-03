# Last updated: 9/3/2026, 9:02:52 AM
1class Solution(object):
2    def findAnagrams(self, s, p):
3        if len(s) < len(p):
4            return []
5        
6        p_count = [0] * 26
7        s_count = [0] * 26
8        
9        for char in p:
10            p_count[ord(char) - ord('a')] += 1
11        
12        result = []
13        for i in range(len(s)):
14            s_count[ord(s[i]) - ord('a')] += 1
15            
16            if i >= len(p):
17                s_count[ord(s[i - len(p)]) - ord('a')] -= 1
18            
19            if s_count == p_count:
20                result.append(i - len(p) + 1)
21        
22        return result