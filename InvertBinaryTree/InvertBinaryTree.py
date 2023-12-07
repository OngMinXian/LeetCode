# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):

        # Edge case
        if not root:
            return root
        
        def dfs(node):
            # Invert operation
            if node.left != None or node.right != None:
                node.left, node.right = node.right, node.left

            # Visit left
            if node.left != None:
                dfs(node.left)

            # Visit right
            if node.right != None:
                dfs(node.right)
        
            return

        dfs(root)

        return root
