class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        rows = len(targetGrid)
        cols = len(targetGrid[0])

        pos = [[rows, cols, 0, 0] for i in range(61)]
        colors = set()

        for i in range(rows):
            for j in range(cols):
                c = targetGrid[i][j]
                colors.add(c)

                pos[c][0] = min(pos[c][0], i)
                pos[c][1] = min(pos[c][1], j)
                pos[c][2] = max(pos[c][2], i)
                pos[c][3] = max(pos[c][3], j)

        def ispossible(c):
            for i in range(pos[c][0], pos[c][2] + 1):
                for j in range(pos[c][1], pos[c][3] + 1):
                    if targetGrid[i][j] > 0 and targetGrid[i][j] != c:
                        return False

            for i in range(pos[c][0], pos[c][2] + 1):
                for j in range(pos[c][1], pos[c][3] + 1):
                    targetGrid[i][j] = 0

            return True

        while colors:
            c2 = set()
            for c in colors:
                if not ispossible(c):
                    c2.add(c)

            if len(c2) == len(colors):
                return False
            
            colors = c2

        return True