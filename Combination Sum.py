class Solution:
    def generate(self,ind,curr,ans,candidates,target):
        if(target==0):
            ans.append(curr.copy())
            return
        if(target<0 or ind==len(candidates)):
            return
        curr.append(candidates[ind])
        self.generate(ind,curr,ans,candidates,target-candidates[ind])
        curr.pop()
        self.generate(ind+1,curr,ans,candidates,target)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ind=0
        curr=[]
        ans=[]
        self.generate(ind,curr,ans,candidates,target)
        return ans
        
