class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)

        for i in range(length):
            nums[(nums[i] % (length+1)) - 1] += (length+1)

        for i in range(length):
            if nums[i] // (length+1) == 0:
                missing = i + 1
            elif nums[i] // (length+1) == 2:
                double = i + 1

        return [double, missing]