# Last updated: 8/11/2026, 6:50:13 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        strlst=list(map(str,s.strip().split(" ")))
        return len(strlst[-1])
        