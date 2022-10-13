class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        ans = [1 for _ in range(length)]

        prefix = 1
        suffix = 1

        for i in range(length):
            ans[i] = prefix
            prefix *= nums[i]

        for i in range(length-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans

