class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob1(arr):
            prev2 = 0
            prev1 = 0
            for num in arr:
                curr = max(prev1, num + prev2)
                prev2 = prev1
                prev1 = curr
            return prev1
        return max(
            rob1(nums[:-1]), 
            rob1(nums[1:])   
        )
