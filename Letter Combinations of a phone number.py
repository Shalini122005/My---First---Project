class Solution:
    def generate(self,ind,curr_str,ans,combos,digits):
        if(ind==len(digits)):
            ans.append(curr_str)
            return
        d_v=int(digits[ind])
        for i in combos[d_v]:
            self.generate(ind+1,curr_str+i,ans,combos,digits)    
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits)==0):
            return []
        ind=0
        curr_str=""
        ans=[]
        combos=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        self.generate(ind,curr_str,ans,combos,digits)
        return ans
        
