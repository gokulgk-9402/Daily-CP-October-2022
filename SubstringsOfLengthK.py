#User function Template for python3
from collections import defaultdict
class Solution:
    def countOfSubstrings(self, S, K):
        # code here 
        ctr = defaultdict(int)
        right = 0
        left = 0
        curr = 0
        
        while right < K:
            if ctr[S[right]] == 0:
                curr += 1
            ctr[S[right]] += 1
            right += 1

            
        ans = 0
        
        if curr == K -1:
            ans += 1
        
        while right < len(S):
            if ctr[S[left]] == 1:
                curr -= 1
            ctr[S[left]] -= 1
                
            if ctr[S[right]] == 0:
                curr += 1
            ctr[S[right]] += 1
                
            if curr == K-1:
                ans += 1
                # print(S[left:right])
                
            right += 1
            left += 1
            
        return ans

print(Solution().countOfSubstrings("gozbbwmrf", 4))