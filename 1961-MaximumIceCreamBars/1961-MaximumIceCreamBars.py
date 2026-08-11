# Last updated: 8/11/2026, 6:36:37 PM
class Solution:
    def maxIceCream(self, costs, coins):
        max_cost = max(costs)

        count = [0] * (max_cost + 1)

        for cost in costs:
            count[cost] += 1

        bars = 0

        for cost in range(1, max_cost + 1):
            if count[cost] == 0:
                continue

            can_buy = min(count[cost], coins // cost)

            bars += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break

        return bars