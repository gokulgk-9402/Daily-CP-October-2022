from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        ans = []

        def findNsum(arr, t, N, temp):
            if len(arr) < N or N < 2:
                return
            
            if N == 2:
                l, r = 0, len(arr) - 1
                while l < r:
                    if arr[l] + arr[r] == t:
                        ans.append(temp + [arr[l], arr[r]])
                        l += 1
                        r -= 1
                        while l < r and arr[l] == arr[l-1]:
                            l += 1
                        while l < r and arr[r] == arr[r+1]:
                            r -= 1
                    elif arr[l] + arr[r] < t:
                        l += 1
                    else:
                        r -= 1

            else:
                for i in range(0, len(arr) - N + 1):
                    if t < arr[i]*N or t > arr[-1]*N:
                        break
                    if i==0 or i > 0 and arr[i-1] != arr[i]:
                        findNsum(arr[i+1:],t-arr[i],N-1,temp+[arr[i]])
 
        findNsum(nums, target, 4, [])

        return ans

print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))