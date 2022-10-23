class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key= lambda x: x[1])
        length = len(pairs)
        ans = 0

        i = 0
        currb = float('-inf')

        while i < length:
            c,d = pairs[i]
            if c > currb:
                ans += 1
                currb = d

            i += 1

        return ans
            