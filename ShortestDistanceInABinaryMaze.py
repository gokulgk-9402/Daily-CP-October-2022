#User function Template for python3

from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        queue = [source]
        rows = len(grid)
        cols = len(grid[0])
        
        distances = {(source[0], source[1]) : 0}
        
        while queue != []:
            r, c= queue.pop(0)
            d = distances[(r,c)]
            
            if r == destination[0] and c == destination[1]:
                return d
            
            if 0<=r-1<rows and grid[r-1][c] == 1:
                queue.append([r-1,c])
                distances[(r-1,c)] = d + 1
            if 0<=r+1<rows and grid[r+1][c] == 1:
                queue.append([r+1,c])
                distances[(r+1,c)] = d + 1
            if 0<=c-1<cols and grid[r][c-1] == 1:
                queue.append([r,c-1])
                distances[(r,c-1)] = d + 1
            if 0<=c+1<cols and grid[r][c+1] == 1:
                queue.append([r,c+1])
                distances[(r,c+1)] = d + 1
            
            grid[r][c] = 0
            
        return -1