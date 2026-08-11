# Last updated: 8/11/2026, 6:48:47 PM
class Solution(object):
    def isPalindrome(self, s):
        s1=""
        for i in s:
            if i.isalnum():
                s1+=i
        return s1.lower() == s1[::-1].lower()