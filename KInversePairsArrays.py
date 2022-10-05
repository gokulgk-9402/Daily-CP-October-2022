class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        mem = [[0 for _ in range(1001)] for _ in range(1001)]

        for i in range(n + 1):
            for j in range(k + 1):
                if j == 0:
                    mem[i][j] = 1
                else:
                    val = MOD + mem[i - 1][j]
                    if j >= i:
                        val -= mem[i-1][j-i]

                    mem[i][j] = (mem[i][j-1] + val) % MOD

        if k > 0:
            return (mem[n][k] + MOD - mem[n][k-1]) % MOD
        
        return (mem[n][k] % MOD)