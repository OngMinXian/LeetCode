# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root) -> int:

        # Edge case
        if not root:
            return 0
        
        def dfs(node, curr_depth):
            # Visit left node
            left_depth = -1
            if node.left != None:
                left_depth = dfs(node.left, curr_depth + 1)

            # Visit right node
            right_depth = -1
            if node.right != None:
                right_depth = dfs(node.right, curr_depth + 1)

            # Return to previous node
            return max(left_depth, right_depth, curr_depth)
        
        return dfs(root, 1)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().maxDepth(root))
