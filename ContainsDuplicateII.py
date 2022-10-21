class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mem = {}
        for i in range(len(nums)):
            if nums[i] in mem:
                if abs(mem[nums[i]] - i) <= k:
                    return True
                else:
                    mem[nums[i]] = i
            else:
                mem[nums[i]] = i

        return False