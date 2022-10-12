class Solution:
    def preimageSizeFZF(self, k: int) -> int:

        def helper(n):
            d = 5
            zeroes = 0
            while d <= n:
                zeroes += n // d
                d *= 5
            return zeroes

        start = 0
        end = int(5* (10**9))

        while start <= end:
            mid = (start + end) // 2
            temp = helper(mid)

            if temp == k:
                return 5
            
            if temp > k:
                end = mid - 1
            else:
                start = mid + 1

        return 0