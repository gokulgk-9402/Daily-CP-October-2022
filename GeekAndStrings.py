# User function Template for Python3

from typing import List
class trie:
    def __init__(self):
        self.children = [None]*26
        self.cnt=0
        
def build(a,root):
    for i in range(len(a)):
        temp=root
        for j in range(len(a[i])):
            if temp.children[ord(a[i][j])-ord("a")] is None:
                temp.children[ord(a[i][j])-ord("a")]=trie()
            temp.children[ord(a[i][j])-ord("a")].cnt+=1
            temp=temp.children[ord(a[i][j])-ord("a")]
            
def find(s,root):
    for i in range(len(s)):
        if root.children[ord(s[i])-ord("a")]==None:
            return 0
        root=root.children[ord(s[i])-ord("a")]
    return root.cnt
    
class Solution:
    def prefixCount(self, N, Q, li, query):
        li=[el[0]for el in li]
        res=[]
        root=trie()
        build(li,root)
        for i in range(Q):
            res.append(find(query[i][0],root))
        return res