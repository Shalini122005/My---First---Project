class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = set()

            for word in level:
                wordSet.discard(word)

            for word in level:
                word_chars = list(word)

                for i in range(len(word)):
                    original = word_chars[i]

                    for ch in ascii_lowercase:
                        if ch == original:
                            continue

                        word_chars[i] = ch
                        new_word = ''.join(word_chars)

                        if new_word in wordSet:
                            next_level.add(new_word)
                            parents[new_word].append(word)

                            if new_word == endWord:
                                found = True

                    word_chars[i] = original

            level = next_level

        if not found:
            return []

        ans = []

        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for parent in parents[word]:
                dfs(parent, path + [parent])

        dfs(endWord, [endWord])

        return ans
