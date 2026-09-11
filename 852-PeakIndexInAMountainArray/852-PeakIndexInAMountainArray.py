# Last updated: 9/11/2026, 9:41:25 AM
class Solution:
    def peakIndexInMountainArray(self, arr):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2

            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            elif arr[mid] > arr[mid + 1]:
                high = mid

        return low