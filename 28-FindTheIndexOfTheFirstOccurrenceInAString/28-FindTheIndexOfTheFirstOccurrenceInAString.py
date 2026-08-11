# Last updated: 8/11/2026, 6:51:06 PM
class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1
        