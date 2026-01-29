class Solution:
    def checkValidString(self, s: str) -> bool:
        minopen=0
        maxopen=0
        n=len(s)
        for c in s:
            if c=='(':
                minopen+=1
                maxopen+=1
            elif c==')':
                minopen-=1
                maxopen-=1
            elif c=="*":
                minopen-=1
                maxopen+=1
            if maxopen<0:
                return False
            if minopen<0:
                minopen=0
        return minopen==0
