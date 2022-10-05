from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val)
            new.left = root
            return new

        q = [(root, 1)]
        while q:
            node, d = q.pop()
            if d == depth - 1:
                l = TreeNode(val, node.left)
                r = TreeNode(val, None, node.right)
                node.left = l
                node.right = r
            else:
                if node.right:
                    q.append((node.right, d + 1))
                if node.left:
                    q.append((node.left, d + 1))

        return root