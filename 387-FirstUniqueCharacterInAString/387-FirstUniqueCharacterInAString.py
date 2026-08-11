# Last updated: 8/11/2026, 6:44:44 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        occu = {}

        for c in s:
            if c in occu:
                occu[c] += 1
            else:
                occu[c] = 1

        for i, c in enumerate(s):
            if occu[c] == 1:
                return i
        else:
            return -1