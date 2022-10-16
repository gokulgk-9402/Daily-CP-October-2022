class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if d > n:
            return -1

        mem_max = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    mem_max[i][j] = jobDifficulty[i]
                else:
                    mem_max[i][j] = max(mem_max[i][j-1], jobDifficulty[j])

        mem = [[0 for _ in range(n)] for _ in range(d)]
        for i in range(d):
            for j in range(i, min(n, n-d+i+1)):
                if i == 0:
                    mem[i][j] = mem_max[i][j]
                else:
                    mem[i][j] = min(mem[i-1][k-1] + mem_max[k][j]
                    for k in range(i, j + 1))
        
        return mem[-1][-1]