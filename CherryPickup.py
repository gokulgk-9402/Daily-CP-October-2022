class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        mem = {}

        def dfs(x1, y1, x2, y2):
            if x1 >= rows or y1 >= cols or x2 >= rows or y2 >= cols or grid[x1][y1] == -1 or grid[x2][y2] == -1:
                return float('-inf')

            if (x1,y1,x2) in mem:
                return mem[(x1,y1,x2)]

            cherries = 0
            if grid[x1][y1] == 1:
                cherries += 1
            
            if grid[x2][y2] == 1 and x1 != x2:
                cherries += 1

            if x1 == rows-1 and y1 == cols-1:
                return cherries

            cherries += max(
                dfs(x1+1,y1,x2+1,y2),
                dfs(x1+1,y1,x2,y2+1),
                dfs(x1,y1+1,x2+1,y2),
                dfs(x1,y1+1,x2,y2+1)
            )

            mem[(x1,y1,x2)] = cherries

            return cherries

        return max(0, dfs(0,0,0,0))