query=[0]*(10001)
flag=False

class Solution:
    def sumOfAll(self, l, r):
        global flag
        def helper():
            query[1]=1
            for i in range(2,10001):
                if query[i]==0:
                    for j in range(2*i,10001,i):
                        query[j]+=i
            query[2]=2
            for i in range(3,10001,2):
                if query[i]==0:
                    query[i]=i
            for i in range(2,10001):
                query[i]+=query[i-1]

        if not flag:
            helper()
            flag=True
            
        return query[r]-query[l-1]
