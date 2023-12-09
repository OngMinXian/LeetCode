# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        # Diameter of a node is max depth of left side + max depth of right side
        def dfs(node):
            if not node:
                return 0, 0
            else:
                left_height, left_dia = dfs(node.left)
                right_height, right_dia = dfs(node.right)
                diameter = left_height + right_height
                return max(left_height, right_height) + 1, max(diameter, left_dia, right_dia)

        return dfs(root)[1]
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
assert Solution().diameterOfBinaryTree(root) == 3
