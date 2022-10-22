class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def valid(d1, d2):
            for key in d2:
                if d1[key] < d2[key]:
                    return False

            return True

        req = defaultdict(int)
        for char in t:
            req[char] += 1

        mem = defaultdict(int)
        right = 0
        ans = ""
        length = len(s)
        minimum = float('inf')

        for left in range(length):
            while right < length and not valid(mem, req):
                mem[s[right]] += 1
                right += 1
            if valid(mem, req):
                if minimum > right - left + 1:
                    minimum = right - left + 1
                    ans = s[left:right]

            mem[s[left]] -= 1

        return ans