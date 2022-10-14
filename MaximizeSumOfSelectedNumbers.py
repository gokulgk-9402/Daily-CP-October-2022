#User function Template for python3
from collections import Counter
class Solution:
    
    def maximizeSum (self,arr, n) : 
        #Complete the function
        mem = Counter(arr)
        a = [False] * n
        ans = 0
        
        for i in range(n-1,-1,-1):
            if a[i] == False:
                a[i] = True
                
                ans += arr[i]
                if mem[arr[i] - 1] > 0:
                    a[i-mem[arr[i]]] = True
                    mem[arr[i] - 1] -= 1
                    
                    
        return ans