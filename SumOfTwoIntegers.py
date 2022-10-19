class Solution:

    def getSum(self, a, b):
        if b == 0:
            return a
        while b:
            tmp = a ^ b
            b = (a & b) << 1
            a = tmp & 0xffffffff
        return a if a >> 31 == 0 else ~(a ^ 0xffffffff)