from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # bfs keep track of curr_k in the state
        m = len(grid)
        n = len(grid[0])
        dist = []
        for r in range(m):
            dist.append([[float('inf')] * (k + 1) for c in range(n)])
        q = deque()
        q.append((0, 0, 0)) # i, j, curr_k
        dist[0][0][0] = 0 # dist[i][j][k] 
        while len(q) > 0:
            i, j, curr_k = q.popleft()
            if curr_k > k:
                continue
            if i == m - 1 and j == n - 1:
                return dist[i][j][curr_k]
            for ni, nj in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                if ni < 0 or ni >= m or nj < 0 or nj >= n:
                    continue
                if grid[ni][nj] == 0:
                    if dist[ni][nj][curr_k] > dist[i][j][curr_k] + 1:
                        dist[ni][nj][curr_k] = dist[i][j][curr_k] + 1
                        q.append((ni, nj, curr_k))
                else:
                    if curr_k + 1 > k:
                        continue
                    if dist[ni][nj][curr_k + 1] > dist[i][j][curr_k] + 1:
                        dist[ni][nj][curr_k + 1] = dist[i][j][curr_k] + 1
                        q.append((ni, nj, curr_k + 1))
        return -1