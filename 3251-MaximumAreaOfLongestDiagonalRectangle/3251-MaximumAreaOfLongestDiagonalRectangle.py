# Last updated: 8/11/2026, 6:34:00 PM
import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        maxi = -1.0
        res = 0
        
        for l, b in dimensions:
            d = math.sqrt(l * l + b * b)
            
            if d > maxi:
                maxi = d
                res = l * b
            elif d == maxi:
                res = max(res, l * b)
        
        return res