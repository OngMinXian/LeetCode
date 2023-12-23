# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        def dfs(node, p, q):
            if node == p or node == q or node == None:
                return node
            else:
                left = dfs(node.left, p, q)
                right = dfs(node.right, p, q)

                if left and right:
                    return node
                else:
                    return left if not right else right
                
        return dfs(root, p , q)
                