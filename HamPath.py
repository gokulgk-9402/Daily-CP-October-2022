#User function Template for python3

class Solution:
    def check(self, N, M, Edges): 
        
        def dfs(u, vis, graph, count, n):
            vis[u] = 1
            if count == n:
                return True
            for v in graph[u]:
                if vis[v] == 0:
                    if dfs(v, vis, graph, count + 1, n):
                        return True
                    vis[v] = 0
            return False
        
        #code here
        visited = [0 for _ in range(N+1)]
        graph = {i: [] for i in range(1, N+1)}
        count = 1
        
        for u, v in Edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(1, N + 1):
            if dfs(i, visited, graph, count, N):
                return True
            visited[i] = 0
        return False


print(Solution().check(4, 4, [[1,2], [2,3], [3,4], [2,4]]))