from collections import deque
from typing import List

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
        maximum = float('-inf')
        q = deque()

        for point in points:
            while q and q[0][1] < point[0] - k:
                q.popleft()
            if q:
                maximum = max(maximum, q[0][0] + point[0] + point[1])
            while q and q[-1][0] <= point[1] - point[0]:
                q.pop()
            q.append([point[1] - point[0], point[0]])

        return maximum