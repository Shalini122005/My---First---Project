class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def ispal(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def bt(start):
            if start==len(s):
                res.append(path[:])
                return 
            for end in range(start,len(s)):
                if ispal(start,end):
                    path.append(s[start:end+1])
                    bt(end+1)
                    path.pop()
        bt(0)
        return res
