class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s) 
        reachable = [False] * n
        reachable[0] = True
        count = 0
        for i in range(1, n):
            if i - minJump >= 0 and reachable[i - minJump]:
                count += 1
            
            if i - maxJump - 1 >= 0 and reachable[i - maxJump - 1]:
                count -= 1
            
            if count > 0 and s[i] == '0':
                reachable[i] = True
        
        return reachable[n - 1]
