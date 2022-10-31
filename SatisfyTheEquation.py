
class Solution:
    def satisfyEqn(self, A, N):
        # code here 
        mem = {}
        ans = [float('inf')] * 4
        flag = False
        
        for i in range(N):
            for j in range(i+1, N):
                cur = A[i] + A[j]
                if cur not in mem:
                    mem[cur] = (i,j)
                else:
                    prev = mem[cur]
                    if prev[0] != i and prev[0] != j and prev[1] != i and prev[1] != j:
                        res = [prev[0],prev[1],i,j]
                        rep = False
                        
                        for p in range(4):
                            if ans[p] < res[p]:
                                break
                            if ans[p] > res[p]:
                                rep = True
                                break
                        if rep:
                            ans = res
        
        if ans[0] == float('inf'):
            return [-1,-1,-1,-1]
        
        return ans
    
 
print(Solution().satisfyEqn([3, 4, 7, 1, 2, 9, 8], 7))