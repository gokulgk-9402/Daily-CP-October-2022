#User function Template for python3
from collections import Counter
class alphanumeric:
    def __init__(self,name,count):
        self.name=name
        self.count=count
class Solution:
    def sortedStrings(self,N,A):
        #code here
        ctr = Counter(A)
        arr = []
        for key in sorted(ctr.keys()):
            arr.append(alphanumeric(key, ctr[key]))
        
        return arr

