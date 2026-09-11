# Last updated: 9/11/2026, 9:30:06 AM
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            while stack:
                g = gcd(stack[-1], num)
                if g == 1:
                    break
                num = (stack.pop() * num) // g
            stack.append(num)

        return stack