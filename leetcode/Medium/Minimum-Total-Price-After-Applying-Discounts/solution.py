"""
LeetCode: Minimum Total Price After Applying Discounts
Difficulty: Medium
Language: Python
Problem: https://leetcode.com/problems/minimum-total-price-after-applying-discounts/
"""

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
