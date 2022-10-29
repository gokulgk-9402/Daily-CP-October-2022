#User function Template for python3
class Solution:
	def leafNodes(self, arr, N):
		# code here
		ans = []
		stack = []
		
		j = 0
		for i in range(1, N):
		    if arr[j] > arr[i]:
		        stack.append(arr[j])
		    else:
		        valid = False
		        while stack:
		            if arr[i] > stack[-1]:
		                stack.pop()
		                valid = True
		            else:
		                break
		        
		        if valid:
		            ans.append(arr[j])
		 
            j += 1
    		i += 1
	
	    ans.append(arr[-1])
	    return ans