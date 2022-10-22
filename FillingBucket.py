#User function Template for python3

class Solution:
    def fillingBucket(self, N):
        # code here
        mem = [0, 1, 2]
        curr = 2
        MOD = 10**8
        
        while curr <= N:
            mem.append((mem[-1] + mem[-2]) % MOD)
            curr += 1
            
        return mem[N] % MOD