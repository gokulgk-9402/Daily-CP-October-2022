class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        n = len(arr)
        def dfs(ind, curr):
            nonlocal ans, n
            if len(curr) == len(set(curr)):
                ans = max(ans, len(curr))
            else:
                return

            for j in range(ind, n):
                dfs(j, curr + arr[j])

        dfs(0, "")
        return ans


"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        curr = [set()]
        arr = [set(a) for a in arr if len(set(a)) == len(a)]

        for a in arr:
            curr += [a|c for c in curr if not a&c]

        return max(len(a) for a in curr)
"""