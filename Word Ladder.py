class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        q=[(beginWord,1)]
        while q:
            word,step=q.pop(0)
            if endWord==word:
                return step
            for i in range(len(word)):
                for ch in 'qwertyuioplkjhgfdaszxcvbnm':
                    newword=word[:i]+ch+word[i+1:]
                    if newword in wordset:
                        q.append((newword,step+1))
                        wordset.remove(newword)
        return 0
