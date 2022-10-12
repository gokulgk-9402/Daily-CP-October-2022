#User function Template for python3


class Solution:
    def maxSum (self, w, x, b, n):
        #code here
        mem = {}
        for i in range(n):
            mem[x[i]] = b[i]
            
        maximum = 0
        max_ending = 0
        left = right = s = 0
        
        if w[0] in mem:
            maximum = mem[w[0]]
        else:
            maximum = ord(w[0])
            
        for i in range(len(w)):
            if w[i] in mem:
                max_ending += mem[w[i]]
            else:
                max_ending += ord(w[i])
                
            if max_ending > maximum:
                maximum = max_ending
                left = s
                right = i
                
            if max_ending < 0:
                max_ending = 0
                s = i + 1
                
        return w[left:right + 1]