# Last updated: 8/11/2026, 6:36:40 PM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26