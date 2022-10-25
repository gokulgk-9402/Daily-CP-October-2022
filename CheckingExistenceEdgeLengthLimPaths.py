class UnionFind:

    def __init__(self, size):
        self.size = size
        self.parents = list(range(size))
        self.sizes = [0] * size

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return

        if self.sizes[rootx] < self.sizes[rooty]:
            small = rootx
            big = rooty
        else:
            small = rooty
            big = rootx

        self.parents[small] = big

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        uf = UnionFind(n)

        edgeList.sort(key=lambda x: x[2])
        answers = [None] * len(queries)

        queries = [(l,u,v,i) for i, (u,v,l) in enumerate(queries)]
        queries.sort(key=lambda x:x[0])

        eidx = 0
        for limit, src, dest, index in queries:
            while eidx < len(edgeList) and edgeList[eidx][2] < limit:
                uf.union(edgeList[eidx][0], edgeList[eidx][1])
                eidx += 1

            answers[index] = uf.find(src) == uf.find(dest)

        return answers