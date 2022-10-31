class Solution:
    def NoOfChicks(self, N):
        # Code here
        
        count = 1
        expires = [0]*50
        expires[6] = 1
        
        for i in range(1, N):
            count -= expires[i]
            expires[i+6] += 2 * count
            count += (2*count)
        
        return count