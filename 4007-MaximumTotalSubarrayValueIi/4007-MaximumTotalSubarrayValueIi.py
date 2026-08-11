# Last updated: 8/11/2026, 6:31:30 PM
import heapq
from typing import List

class SparseTable:
    def __init__(self, arr: List[int]):
        n = len(arr)
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1
        max_log = self.log[n] + 1

        self.min_table = [[0] * max_log for _ in range(n)]
        self.max_table = [[0] * max_log for _ in range(n)]

        for i in range(n):
            self.min_table[i][0] = self.max_table[i][0] = arr[i]

        j = 1
        while (1 << j) <= n:
            for i in range(n - (1 << j) + 1):
                self.min_table[i][j] = min(
                    self.min_table[i][j - 1],
                    self.min_table[i + (1 << (j - 1))][j - 1]
                )
                self.max_table[i][j] = max(
                    self.max_table[i][j - 1],
                    self.max_table[i + (1 << (j - 1))][j - 1]
                )
            j += 1

    def query_min(self, left: int, right: int) -> int:
        j = self.log[right - left + 1]
        return min(self.min_table[left][j], self.min_table[right - (1 << j) + 1][j])

    def query_max(self, left: int, right: int) -> int:
        j = self.log[right - left + 1]
        return max(self.max_table[left][j], self.max_table[right - (1 << j) + 1][j])


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sparse_table = SparseTable(nums)
        total_value = 0

  
        heap = [
            (-(sparse_table.query_max(0, i) - sparse_table.query_min(0, i)), 0, i)
            for i in range(n)
        ]
        heapq.heapify(heap)

        for _ in range(k):
            value, left, right = heapq.heappop(heap)
            total_value -= value  
            if left + 1 <= right:
                new_value = sparse_table.query_max(left + 1, right) - sparse_table.query_min(left + 1, right)
                heapq.heappush(heap, (-new_value, left + 1, right))

        return total_value