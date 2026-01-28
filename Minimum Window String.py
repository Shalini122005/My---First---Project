class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        freq={}
        n=len(s)
        for ch in t:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        left=0
        minl=float('inf')
        count=0
        start=0
        for r in range(n):
            if s[r] in freq:
                if freq[s[r]]>0:
                    count+=1
                freq[s[r]]-=1
            else:
                freq[s[r]]=-1
            while count==len(t):
                if r-left+1<minl:
                    minl=r-left+1
                    start=left
                freq[s[left]]+=1
                if freq[s[left]]>0:
                    count-=1
                left+=1
        if minl==float('inf'):
            return ""
        else:
            return s[start:start+minl]
            
