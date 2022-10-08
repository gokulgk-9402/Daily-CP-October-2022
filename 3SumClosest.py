class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        ans = float('inf')
        diff = float('inf')

        nums.sort()

        for i in range(length):
            start = i + 1
            end = length - 1

            while start < end:
                curr = nums[i] + nums[start] + nums[end]
                if diff > abs(target-curr):
                    ans = curr
                    diff = abs(target - curr)

                if curr == target:
                    break
                
                if curr > target:
                    end -= 1
                else:
                    start += 1

        return ans