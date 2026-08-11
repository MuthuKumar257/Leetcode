# Last updated: 8/11/2026, 6:33:13 PM
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