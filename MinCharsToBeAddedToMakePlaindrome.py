class Solution:
    def minChar(self,str):
        #Write your code here
        def LPS(string):
            m = len(string)
            lps = [None]*m
            
            length = 0
            lps[0] = 0
            
            i = 1
            while i < m:
                if string[i] == string[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length!= 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
            
        rev = str[::-1]
        s = str + "$" + rev
        lps = LPS(s)
        
        return len(str) - lps[-1]