# Last updated: 8/11/2026, 6:47:49 PM
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for char in columnTitle:
            col_num = col_num * 26 + (ord(char) - 64)
        return col_num