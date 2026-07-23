class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        res = []
        p_count = [0] * 26
        window = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        for i in range(len(s)):
            window[ord(s[i]) - ord('a')] += 1

            if i >= len(p):
                window[ord(s[i - len(p)]) - ord('a')] -= 1

            if window == p_count:
                res.append(i - len(p) + 1)

        return res
