from math import sqrt, pi, cos, sin
from typing import List

class Solution:
    def getMinDistSum(self, P: List[List[int]]) -> float:
        def helper(x, y):
            return sum(sqrt((x2-x)**2 + (y2-y)**2) for x2, y2 in P)

        length = len(P)
        x, y = sum(x for x, y in P) / length, sum(y for x, y in P) / length
        minimum = helper(x, y)
        
        step, eps = 10, 0.000001
        div = 5

        theta = 2 * pi / div
        while step > eps:
            for i in range(div):
                dx, dy = cos(theta*i), sin(theta*i)
                x2, y2 = x + step * dx, y + step * dy
                curr = helper(x2, y2)
                if curr < minimum:
                    x, y, minimum = x2, y2, curr
                    flag = True
                    break
            else:
                step /= 2
        return minimum