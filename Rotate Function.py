class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        f = 0
        for i in range(n):
            f += i * nums[i]

        ans = f

        for i in range(n - 1, 0, -1):
            f = f + total - n * nums[i]
            ans = max(ans, f)

        return ans
