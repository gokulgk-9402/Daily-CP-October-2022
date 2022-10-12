class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        i = 2
        length = len(nums)

        while i < len(nums):
            if nums[i-2] < nums[i-1] + nums[i]:
                return nums[i] + nums[i-1] + nums[i-2]
            i += 1
        return 0