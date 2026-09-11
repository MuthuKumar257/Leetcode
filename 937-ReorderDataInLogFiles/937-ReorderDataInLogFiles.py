# Last updated: 9/11/2026, 9:40:29 AM
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def customSort(log):
            idx = log.index(' ') + 1
            if log[idx].isalpha():
                return (0, log[idx:], log[:idx])
            return (1,)

        return sorted(logs, key=customSort)