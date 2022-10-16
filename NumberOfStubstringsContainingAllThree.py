class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        right = 0

        mem = {}
        count = 0

        while right < len(s):
            end = s[right]
            mem[end] = mem.get(end, 0) + 1

            while len(mem) == 3 and left < right:
                start = s[left]
                count += len(s) - right
                mem[start] -= 1
                if mem[start] == 0:
                    mem.pop(start)

                left += 1
            right += 1
        return count