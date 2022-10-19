class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        t121 = 6
        t123 = 6

        for i in range(n-1):
            t121, t123 = (t121 * 3 + t123 * 2) % MOD, (t121 * 2 + t123 * 2) % MOD

        return (t121 + t123) % MOD