# Last updated: 8/11/2026, 6:46:54 PM
class Solution(object):
    def rob(self, nums):
        rob, norob = 0, 0
        for num in nums:
            newRob = norob + num
            newNoRob = max(norob, rob)
            rob, norob = newRob, newNoRob
        return max(rob, norob)
        