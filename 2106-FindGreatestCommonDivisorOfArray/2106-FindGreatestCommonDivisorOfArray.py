# Last updated: 8/11/2026, 6:36:16 PM
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        smallest = min(nums)
        largest = max(nums)

        return math.gcd(smallest, largest)