# Last updated: 9/11/2026, 9:32:23 AM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26