class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        length = len(arr)

        rems = defaultdict(int)

        for i in range(length):
            rems[arr[i]%k] += 1

        if k % 2 == 0:
            if rems[k//2] % 2:
                return False

        for i in range(1, k//2 + 1):
            if rems[i] != rems[k-i]:
                return False

        return True