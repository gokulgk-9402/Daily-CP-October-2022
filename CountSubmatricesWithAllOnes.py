from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        cols = len(mat[0])
        h = [0] * cols
        ans = 0

        for row in mat:
            mem = []
            for i in range(cols):
                h[i] = (row[i] == 1) * (h[i] + 1)
                while mem and h[i]<h[mem[-1][0]]:
                    mem.pop()

                ct = (i - mem[-1][0]) * h[i] + mem[-1][1] if mem else h[i]*(i+1)

                ans += ct
                mem.append((i, ct))

        return ans
