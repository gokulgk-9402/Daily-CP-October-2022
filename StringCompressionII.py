class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        def helper(index, res_k, carry = 0):

            if carry == 0 and mem[index][res_k] != -1:
                return mem[index][res_k]

            curr = carry + frequency[index]
            minimum = 1 + min(len(str(curr)), curr - 1) + helper(index+1, res_k)

            for leave, code in [(0,0),(1,1),(9,2),(99,3)]:
                if curr > leave and res_k >= curr - leave:
                    minimum = min(minimum, code + helper(index+1,res_k + leave - curr))

            next = chars.find(chars[index], index+1)
            delete = sum(frequency[index+1:next])
            if next > 0 and res_k >= delete:
                minimum = min(minimum, helper(next, res_k - delete, curr))

            if carry == 0:
                mem[index][res_k] = minimum
            
            return minimum

        frequency = []
        chars = ""

        for char in s:
            if len(frequency) == 0 or char != chars[-1]:
                frequency.append(0)
                chars = chars + char

            frequency[-1] += 1

        mem = [[-1] * (k+1) for i in range(len(frequency))] + [[0] * (k+1)]

        return helper(0, k)