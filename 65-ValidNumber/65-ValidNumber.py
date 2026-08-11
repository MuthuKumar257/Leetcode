# Last updated: 8/11/2026, 6:50:04 PM
class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match(r'^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$',s))