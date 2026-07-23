class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        word_map = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            n = len(word)

            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]

                # Case 1: Prefix is palindrome
                if is_palindrome(prefix):
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_map and word_map[rev_suffix] != i:
                        result.append([word_map[rev_suffix], i])

                # Case 2: Suffix is palindrome
                # j != n avoids duplicates
                if j != n and is_palindrome(suffix):
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_map and word_map[rev_prefix] != i:
                        result.append([i, word_map[rev_prefix]])

        return result
