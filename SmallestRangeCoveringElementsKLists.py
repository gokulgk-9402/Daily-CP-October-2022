class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        length = len(nums)

        ans = []
        h = [(lst[0], i, 0) for i, lst in enumerate(nums)]
        heapq.heapify(h)

        right = max(lst[0] for lst in nums)
        while h:
            left, i, j = heapq.heappop(h)
            if not ans or right - left < ans[1] - ans[0]:
                ans = [left, right]
            if j + 1 == len(nums[i]):
                return ans

            right = max(right, nums[i][j+1])
            heapq.heappush(h, (nums[i][j+1], i, j + 1))

        return ans