from typing import List
from collections import defaultdict

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        mem = defaultdict(int)
        
        for a in nums:
            for b in nums:
                mem[a&b] += 1

        ans = 0

        for key in mem:
            for c in nums:
                
                if key & c == 0:
                    ans += mem[key]

        return ans