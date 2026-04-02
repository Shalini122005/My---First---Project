class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for course,dest in prerequisites:
            graph[dest].append(course)
            indegree[course]+=1
        q=[]
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        finish=[]
        while q:
            node=q.pop(0)
            finish.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(finish)==numCourses:
            return finish
        return []
