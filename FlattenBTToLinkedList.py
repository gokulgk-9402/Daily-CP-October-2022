#User function Template for python3

class Solution:
    def flatten(self, root):
        #code here
        
        def helper(node):
            if not node:
                return None
                
            temp = helper(node.right)
            node.right = helper(node.left)
            node.left = None
            
            t2 = node
            while t2.right is not None:
                t2 = t2.right
                
            t2.right = temp
            
            return node
            
        return helper(root)

