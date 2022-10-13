class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = []
        ans = []

        for i in range(len(nums)):
            if queue and queue[0] < i - k + 1:
                queue.pop(0)

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if queue and i >= k - 1:
                ans.append(nums[queue[0]])

        return ans