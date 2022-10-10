#User function Template for python3

from typing import List

import heapq

class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # code here
        
        root = [i for i in range(rows*cols)]
        rank = [1] * (rows*cols)
        
        mat = [[0 for _ in range(cols)] for _ in range(rows)]
        
        def find(x):
            if root[x] == x:
                return x
                
            root[x] = find(root[x])
            return root[x]
            
        def union(x,y):
            x, y = find(x), find(y)
            if x == y:
                return False
                
            if rank[x] > rank[y]:
                root[y] = x
            elif rank[y] > rank[x]:
                root[x] = y
            else:
                root[y] = x
                rank[x] += 1
                
            return True
            
        ans = [1]
        mat[operators[0][0]][operators[0][1]] = 1
        
        for x, y in operators[1:]:
            if mat[x][y]:
                ans.append(ans[-1])
                continue
            
            mat[x][y] = count = 1
            for i,j in [(0,-1),(0,1),(1,0),(-1,0)]:
                p,q = i+x,y+j
                if 0<= p<rows and 0<= q<cols and mat[p][q]:
                    count -= union(x*cols+y, p*cols+q)
                    
            ans.append(ans[-1] + count)
            
        return ans