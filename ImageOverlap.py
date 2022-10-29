class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ones_1 = []
        ones_2 = []

        mem = defaultdict(int)

        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones_1.append((i,j))
                if img2[i][j] == 1:
                    ones_2.append((i,j))

        for x1, y1 in ones_1:
            for x2, y2 in ones_2:
                mem[(x1-x2,y1-y2)] += 1

        if mem:
            return max(mem.values())
        
        return 0