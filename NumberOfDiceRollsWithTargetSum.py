class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        mem = [[0 for _ in range(max(k+1, target + 1))] for _ in range(n)]
        for i in range(k):
            mem[0][i+1] += 1

        for roll in range(1, n):
            for prev in range(target + 1):
                for curr in range(1, k+ 1):
                    if prev + curr <= target:
                        mem[roll][prev + curr] += mem[roll-1][prev]
                        mem[roll][prev + curr] %= MOD

        return mem[n-1][target]

print(Solution().numRollsToTarget(30, 30, 500))