class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        need = Counter()

        for word in words2:
            c = Counter(word)
            for ch in c:
                need[ch] = max(need[ch], c[ch])

        ans = []

        for word in words1:
            c = Counter(word)
            ok = True
            for ch in need:
                if c[ch] < need[ch]:
                    ok = False
                    break
            if ok:
                ans.append(word)

        return ans
