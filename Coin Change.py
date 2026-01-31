class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for i in coins:
            for j in range(i,amount+1):
                dp[j]=min(dp[j],1+dp[j-i])
        if dp[amount]!=(amount+1):
            return dp[amount]
        else:
            return -1

