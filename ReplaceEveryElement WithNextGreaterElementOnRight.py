from typing import List
from sortedcontainers import SortedList

class Solution:
    def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
        # code here
        s = SortedList([])
        ans = [0] * n
        
        for i in range(n-1, -1, -1):
            ind = s.bisect_right(arr[i])
            if ind == len(s):
                ans[i] = -1
            else:
                ans[i] = s[ind]
            
            s.add(arr[i])
            
        return ans