#User function Template for python3
class Solution:
    def lexicographicallySmallest (ob, S, k):
        # code here 
        length = len(S)
        if length & (length-1) == 0:
            k = k//2
        else:
            k = k*2
            
        if length<=k:
            return -1
            
        req = length-k
        stack = []
        for i in range(length):
            while stack and stack[-1] > S[i] and len(stack) + length - i - 1 >= req:
                stack.pop()
            if len(stack) < req or stack[-1] > S[i]:
                stack.append(S[i])
                
        return "".join(stack)