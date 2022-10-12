from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        length = len(nums)
        change = [1] * length

        for i in range(length):
            change[(i-nums[i]+1)%length] -= 1
        for i in range(1, length):
            change[i] +=  change[i-1]
        
        return change.index(max(change))