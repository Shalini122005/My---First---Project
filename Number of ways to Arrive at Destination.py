class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))  
        dist = [float('inf')] * n
        ways = [0] * n     
        dist[0] = 0
        ways[0] = 1
        pq = [(0, 0)]  
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for nei, wt in adj[node]:
                new_dist = d + wt
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_dist, nei))
                elif new_dist == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        return ways[n - 1] % MOD
