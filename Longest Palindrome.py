class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd = False

        for v in count.values():
            if v % 2 == 0:
                length += v
            else:
                length += v - 1
                odd = True

        if odd:
            length += 1

        return length
