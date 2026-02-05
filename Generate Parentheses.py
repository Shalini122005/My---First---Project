class Solution:
    def generate(self,ind,curr_str,o,c,n,ans):
        if(o>n):
            return
        if(ind==2*n and o==c):
            ans.append(curr_str)
            return
        self.generate(ind+1,curr_str+"(",o+1,c,n,ans)
        if(o>c):
            self.generate(ind+1,curr_str+")",o,c+1,n,ans)
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        o=0
        c=0
        ind=0
        curr_str=""
        self.generate(ind,curr_str,o,c,n,ans)
        return ans
