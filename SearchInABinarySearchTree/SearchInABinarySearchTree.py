# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root, val: int):

        self.found_node = None
        def binary_search(node, val, res=False):
            # Found value already, just return
            if self.found_node != None:
                return
            
            # Found value
            if node.val == val:
                self.found_node = node
            
            # Value is smaller, visit left
            elif node.val > val and node.left != None:
                binary_search(node.left, val)

            # Value is larger, visit right
            elif node.val < val and node.right != None:
                binary_search(node.right, val)

        binary_search(root, val)

        return self.found_node
        
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(Solution().searchBST(root, 2))
