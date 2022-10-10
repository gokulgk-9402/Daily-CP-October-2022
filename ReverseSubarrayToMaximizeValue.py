class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        total = 0
        ans = 0
        minimum = float('inf')
        maximum = -float('inf')

        for a,b in zip(nums, nums[1:]):
            total += abs(a - b)

            ans = max(ans, abs(nums[0]-b) - abs(a-b))
            ans = max(ans, abs(nums[-1]-a) - abs(a-b))

            minimum = min(minimum, max(a,b))
            maximum = max(maximum, min(a,b))

        return total + max(ans, (maximum-minimum) * 2)