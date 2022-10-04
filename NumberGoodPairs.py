from typing import List
import math
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        ans = 0
        length = len(nums)

        c = Counter(nums)

        for key in c:
            if c[key] >= 2:
                ans += math.comb(c[key], 2)

        return ans