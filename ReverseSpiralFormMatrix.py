#User function Template for python3
class Solution:
    def reverseSpiral(self, R, C, a):
		# code here
		ans = []
		
		i = j = 0
		
		while i < R and j < C:
		    for col in range(j, C):
		        ans.append(a[i][col])
            i += 1
            
            for row in range(i, R):
                ans.append(a[row][C-1])
                
            C -= 1
            
            if i < R:
                for col in range(C-1, j-1, -1):
                    ans.append(a[R-1][col])
                R -= 1
                
            if j < C:
                for row in range(R-1, i-1, -1):
                    ans.append(a[row][j])
                j += 1
                
        return ans[::-1]