# Last updated: 8/22/2026, 9:14:24 AM
1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        sum_digit = 0
4        product_digit = 1
5        num = n
6
7
8        while num > 0:
9            sum_digit += num % 10
10            product_digit *= num % 10
11            num //= 10
12
13
14        return n % (sum_digit + product_digit) == 0