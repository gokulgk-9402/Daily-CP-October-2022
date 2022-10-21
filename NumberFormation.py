#User function Template for python3
class Solution:
    def getSum(self, X, Y, Z):
		# code here
		MOD = 10**9 + 7
		
		exactsum = [[[0] * (Z + 1) for _ in range(Y+1)] for _ in range(X+1)]
		exactnum = [[[0] * (Z + 1) for _ in range(Y+1)] for _ in range(X+1)]
		
		ans = 0
		exactnum[0][0][0] = 1
		
		for i in range(X+1):
		    for j in range(Y+1):
		        for k in range(Z+1):
		            
		            if i > 0:
		                exactsum[i][j][k] += (exactsum[i-1][j][k] * 10 + 4 * exactnum[i-1][j][k])% MOD
		                exactnum[i][j][k] += exactnum[i-1][j][k] % MOD
		            if j > 0:
		                exactsum[i][j][k] += (exactsum[i][j-1][k] * 10 + 5 * exactnum[i][j-1][k])% MOD
		                exactnum[i][j][k] += exactnum[i][j-1][k] % MOD
		            if k > 0:
		                exactsum[i][j][k] += (exactsum[i][j][k-1] * 10 + 6 * exactnum[i][j][k-1])% MOD
		                exactnum[i][j][k] += exactnum[i][j][k-1] % MOD
		                
		            ans += exactsum[i][j][k]
		            ans %= MOD
		            
	    return ans