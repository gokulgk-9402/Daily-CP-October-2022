class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        mem = {
            0: 1,
            1: 0,
            2: 0,
            3: 0
        }

        for num in nums:
            mem[num + 1] = (mem[num] + mem[num + 1] * 2) % MOD

        return mem[3]