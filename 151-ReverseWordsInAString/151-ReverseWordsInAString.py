# Last updated: 8/11/2026, 6:48:19 PM
class Solution(object):
    def reverseWords(self, s):
        a=list(s.split())
        a=a[::-1]
        return " ".join(a)