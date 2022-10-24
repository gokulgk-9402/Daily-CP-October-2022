class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = 0
        i = 0
        length = len(s)

        def helper(left, right):
            nonlocal ans
            while left>= 0 and right < length and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1

        while i < length:
            helper(i, i)
            helper(i-1, i)

            i += 1

        return ans