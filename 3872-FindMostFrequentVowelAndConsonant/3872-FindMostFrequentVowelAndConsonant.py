# Last updated: 8/11/2026, 6:31:53 PM
class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq=Counter(s)
        v_max=0
        c_max=0
        for ch in 'aeiou':
            if ch in freq:
                v_max=max(v_max,freq[ch])
                del freq[ch]
        
        for (key,val) in freq.items():
            c_max=max(c_max,val)
        
        return v_max+c_max