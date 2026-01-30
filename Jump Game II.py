class Solution:
    def jump(self, nums: List[int]) -> int:
        j=0
        f=0
        c=0
        n=len(nums)
        for i in range(n-1):
            f=max(f,nums[i]+i)
            if i==c:
                j+=1
                c=f
        return j
