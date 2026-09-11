# Last updated: 9/11/2026, 9:31:29 AM
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        smallest = min(nums)
        largest = max(nums)

        return math.gcd(smallest, largest)