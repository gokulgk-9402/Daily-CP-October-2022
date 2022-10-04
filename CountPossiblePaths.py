#User function Template for python3
import math
class Solution:
    def numberOfPaths(self, m, n):
        MOD = 10**9 + 7
		# code here
        def factorial(num):
            res = 1
            for i in range(2, num + 1):
                res *= i
            return res
		    
        return (factorial(n+m - 2) // (factorial(n - 1) * factorial(m - 1))) % MOD