#User function Template for python3
from collections import Counter

class Solution:
    def minFind(self, n, a):
        # code here
        ctr = Counter(a)
        
        if ctr['R'] == n or ctr['G'] == n or ctr['B'] == n:
            return n
            
        if ctr['R']&1 == 0 and ctr['G']&1 == 0 and ctr['B']&1 == 0:
            return 2
        elif ctr['R']&1 != 0 and ctr['G']&1 != 0 and ctr['B']&1 != 0:
            return 2
        else:
            return 1