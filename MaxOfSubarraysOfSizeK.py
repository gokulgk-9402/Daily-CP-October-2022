#User function Template for python3
from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        #code here
        ans = []
        dq = deque()
        
        for i in range(k):
            while len(dq) and arr[i]>=arr[dq[-1]]:
                dq.pop()
            dq.append(i)
            
        for i in range(k, n):
            ans.append(arr[dq[0]])
            while len(dq) and dq[0]<=i-k:
                dq.popleft()
                
            while len(dq) and arr[i]>=arr[dq[-1]]:
                dq.pop()
                
            dq.append(i)
            
        ans.append(arr[dq[0]])
        dq.popleft()
        
        return ans