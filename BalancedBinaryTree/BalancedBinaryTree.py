# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root) -> bool:
        
        def dfs(node):
            # Return
            if not node:
                return True, 0

            # Visit left and right
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            # Check height balanced when returning
            balanced = True
            if abs(left_height - right_height) > 1:
                balanced = False

            return (balanced and left_balanced and right_balanced), (max(left_height, right_height) + 1)

        return dfs(root)[0]
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)
root.left.left.right = TreeNode(7)
print(Solution().isBalanced(root))
