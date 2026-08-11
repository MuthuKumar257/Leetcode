# Last updated: 8/11/2026, 6:29:55 PM
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        res=0.0
        for i in range(len(prices)):
            if i<len(discounts):
                res+=prices[i]*(100-discounts[i])/100
            else:
                res+=prices[i]
        return res