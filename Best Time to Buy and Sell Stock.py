class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=float('inf')
        maxp=0
        for p in prices:
            mp=min(mp,p)
            maxp=max(maxp,p-mp)
        return maxp
