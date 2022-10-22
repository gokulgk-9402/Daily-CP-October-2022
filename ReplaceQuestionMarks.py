class Solution:
    def modifyString(self, s: str) -> str:
        length = len(s)
        ans = ""
        prev = "?"

        for i, char in enumerate(s):
            next = s[i+1] if i + 1 < length else '?'
            prev = char if char != '?' else {'a', 'b', 'c'}.difference({prev, next}).pop()
            ans += prev

        return ans