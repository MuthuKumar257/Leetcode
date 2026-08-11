# Last updated: 8/11/2026, 6:50:00 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, 2) + int(b, 2):b}"