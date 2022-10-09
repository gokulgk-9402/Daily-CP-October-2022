# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
        # print(inorder)
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] + arr[right] == k:
                return True

            elif arr[left] + arr[right] > k:
                right -= 1
            
            else:
                left += 1

        return False