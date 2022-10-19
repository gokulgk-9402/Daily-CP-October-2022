from typing import List
import math

class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        def distance(x1, y1, x2, y2):
            return math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)

        dia = 2 * r
        num = len(darts)
        maximum = 1
        for i in range(num):
            p1x, p1y = darts[i]
            for j in range(i+1, num):
                p2x, p2y = darts[j]

                d = distance(p1x, p1y, p2x, p2y)

                if d < dia:
                    dx, dy = p2x - p1x, p2y - p1y
                    tx, ty = (p1x + p2x)/2 , (p1y + p2y)/2
                    perpen = math.sqrt(r**2 - (d/2)**2)
                    c1x, c1y = (tx - perpen*dy/d), (ty + perpen*dx/d)
                    c2x, c2y = (tx + perpen*dy/d), (ty - perpen*dx/d)

                    curr = 0
                    for dart in darts:
                        if distance(dart[0], dart[1], c1x, c1y) <= r:
                            curr += 1
                    
                    maximum = max(maximum, curr)

                    curr = 0
                    for dart in darts:
                        if distance(dart[0], dart[1], c2x, c2y) <= r:
                            curr += 1
                    
                    maximum = max(maximum, curr)


                elif d == dia:
                    cx, cy = (p1x + p2x)/2 , (p1y + p2y)/2
                    curr = 0
                    for dart in darts:
                        if distance(dart[0], dart[1], cx, cy) <= r:
                            curr += 1

                    maximum = max(maximum, curr)

                if maximum == num:
                    return maximum

        return maximum



