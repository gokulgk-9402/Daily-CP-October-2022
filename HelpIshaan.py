#User function Template for python3

class Solution:
    def NthTerm(self, N):
	    if N == 1:
	        return 1
		# Code here
		def isprime(num):
		    if num == 2:
		        return True
		    if num < 2:
		        return False
		        
		    i = 2
		    while i*i <= num:
		        if num % i == 0:
		            return False
		        i += 1
		            
		    return True
		    
	    t = 0
	    while t < N:
	        # print(N, t)
	        # print(isprime(N-t))
	        # print(isprime(N+t))
	        if isprime(N-t) or isprime(N+t):
	            return t
	        t += 1