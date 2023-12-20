# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        
        def in_order_traversal(node):
            if not node:
                return []
            else:
                return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

        order = in_order_traversal(root)
        prev = order[0]
        for i in range(1, len(order)):
            if order[i] <= prev:
                return False
            prev = order[i]

        return True

class Solution:
    def isValidBST(self, root) -> bool:
        
        def dfs(node, upper_bound, lower_bound):
            if not node:
                return True
            else:
                if lower_bound < node.val < upper_bound:
                    return dfs(node.left, node.val, lower_bound) and dfs(node.right, upper_bound, node.val)
                else:
                    return False
            
        return dfs(root, 2**31, -2**31-1)

test1 = TreeNode(8)
test1.left = TreeNode(-70)
test1.right = TreeNode(81)
print(Solution().isValidBST(test1))
