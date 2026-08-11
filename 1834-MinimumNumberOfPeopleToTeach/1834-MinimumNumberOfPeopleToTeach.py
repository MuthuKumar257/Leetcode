# Last updated: 8/11/2026, 6:36:52 PM
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        langs = [set(x) for x in languages]
        bad = set()
        for u, v in friendships:
            if langs[u-1].isdisjoint(langs[v-1]):
                bad.add(u-1)
                bad.add(v-1)
        if not bad:
            return 0
        ans = float('inf')
        for lang in range(1, n+1):
            cnt = 0
            for i in bad:
                if lang not in langs[i]:
                    cnt += 1
            ans = min(ans, cnt)
        return ans