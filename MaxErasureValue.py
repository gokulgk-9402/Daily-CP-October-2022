from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        seen = set()

        ans = 0
        current = 0

        left = 0

        for num in nums:
            while num in seen:
                current -= nums[left]
                seen.remove(nums[left])
                left += 1
            
            current += num
            seen.add(num)
            ans = max(ans, current)

        return ans