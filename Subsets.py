class Solution:
    def generate(self,ind,curr,ans,nums):
        if(ind==len(nums)):
            ans.append(curr.copy())
            return
        curr.append(nums[ind])
        #take
        self.generate(ind+1,curr,ans,nums)
        curr.pop()
        #not take
        self.generate(ind+1,curr,ans,nums)    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        curr=[]
        ind=0
        self.generate(ind,curr,ans,nums)
        return ans
