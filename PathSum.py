# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def helper(node, s):
            if node.right == None and node.left == None:
                if node.val == s:
                    return True
                
                return False

            flag = False
            if node.right:
                flag = flag or helper(node.right, s - node.val)
            if node.left:
                flag = flag or helper(node.left, s - node.val)

            return flag

        return helper(root, targetSum)