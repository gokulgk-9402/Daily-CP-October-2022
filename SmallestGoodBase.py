class Solution:
    def smallestGoodBase(self, n: str) -> str:
        s = 1
        n = int(n)
        ans = n - 1

        while s < 61:
            left = 2
            right = 10**18

            while left <= right:
                mid = (left+right)//2
                num = (mid**s - 1)//(mid-1)
                if num == n:
                    if mid < ans:
                        ans = mid
                    right = mid - 1
                else:
                    if num > n:
                        right = mid - 1
                    else:
                        left = mid + 1

            s += 1

        return str(ans)
                        