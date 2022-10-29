#User function Template for python3

class Solution:
	def NthTerm(self, n):
		# Code here
		MOD = 10**9 + 7
		ans = 1
		for i in range(1, n+1):
		    ans = ans*i + 1
		    ans = ans % MOD
		    
		return ans