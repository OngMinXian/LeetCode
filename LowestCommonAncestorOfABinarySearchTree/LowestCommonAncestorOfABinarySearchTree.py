# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        self.res = None

        def dfs(node):
            # Return to parent
            if node == None or self.res != None:
                return

            # LCA on left side
            if p.val < node.val and q.val < node.val:
                dfs(node.left)

            # LCA on right side
            elif p.val > node.val and q.val > node.val:
                dfs(node.right)

            else:
                self.res = node
                return

        dfs(root)

        return self.res
