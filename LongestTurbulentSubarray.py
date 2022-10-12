class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 0
        curr = 0

        for i in range(len(arr)):
            if i >= 2 and (arr[i-2] > arr[i-1] < arr[i] or arr[i-2] < arr[i-1] > arr[i]):
                curr += 1
            elif i >= 1 and arr[i-1] != arr[i]:
                curr = 2
            else:
                curr = 1

            ans = max(ans, curr)

        return ans
