# Last updated: 9/11/2026, 9:25:14 AM
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        visited = set()

        result = []
        for num in nums:
            if(num not in visited):
                visited.add(num)
            else:
                result.append(num)

        return result