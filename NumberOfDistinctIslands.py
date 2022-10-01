import sys
from typing import List
sys.setrecursionlimit(10**8)

class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r0, c0, r, c, v):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            if grid[r][c] == 1:
                grid[r][c] = 0
                v.append((r-r0, c-c0))
                dfs(r0, c0, r+1, c, v)
                dfs(r0, c0, r-1, c, v)
                dfs(r0, c0, r, c+1, v)
                dfs(r0, c0, r, c-1, v)
                
            return
        
        coordinates = set()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    v = []
                    dfs(i, j, i, j, v)
                    coordinates.add(tuple(v))

        return len(coordinates)