class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = max_sum = nums[0]

        for num in nums[1:]:
            curr = max(num, curr + num)
            max_sum = max(max_sum, curr)

        return max_sum
