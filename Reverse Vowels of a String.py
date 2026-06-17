class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"

        chars = list(s)
        rev_vowels = [ch for ch in s if ch in vowels][::-1]

        j = 0
        for i in range(len(chars)):
            if chars[i] in vowels:
                chars[i] = rev_vowels[j]
                j += 1

        return "".join(chars)
