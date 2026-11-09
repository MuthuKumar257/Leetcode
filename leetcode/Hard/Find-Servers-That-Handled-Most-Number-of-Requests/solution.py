"""
LeetCode: Find Servers That Handled Most Number of Requests
Difficulty: Hard
Language: Python
Problem: https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
"""

freq = [0]*k
        
        for i, (ta, tl) in enumerate(zip(arrival, load)): 
            while busy and busy[0][0] <= ta: 
                _, ii = heappop(busy)
                heappush(free, i + (ii - i) % k) # circularly relocate it
            if free: 
                ii = heappop(free) % k 
                freq[ii] += 1
                heappush(busy, (ta+tl, ii))
        
        mx = max(freq)
        return [i for i, x in enumerate(freq) if x == mx]
