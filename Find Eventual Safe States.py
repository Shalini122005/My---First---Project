class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        states=[0]*n
        def dfs(node):
            if states[node]!=0:
                return states[node]==2
            states[node]=1
            for nei in graph[node]:
                if states[nei]==1 or not dfs(nei):
                    return False
            states[node]=2
            return True
        res=[]
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
