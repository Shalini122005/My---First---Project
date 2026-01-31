class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones)<=2:
            return stones[-1]
        ans=0
        for i in range(2,len(stones)):
            ans=max(ans,stones[i]-stones[i-2])
        return ans
