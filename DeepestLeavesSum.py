from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        queue = [(root, 1)]
        depth = 0
        ans = 0

        while queue:
            print(queue)
            node, d = queue.pop(0)

            if (not node.left) and (not node.right):
                if d == depth:
                    ans += node.val
                elif d > depth:
                    depth = d
                    ans = node.val

            if node.left:
                queue.append((node.left, d + 1))
            if node.right:
                queue.append((node.right, d + 1))

        return ans

