# Last updated: 8/11/2026, 6:36:06 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if op[1]=='+' else -1 for op in operations)