# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):

        indexer = {}
        for i in range(len(inorder)):
            indexer[inorder[i]] = i

        def helper(preorder, inorder_left, inorder_right):
            if inorder_left > inorder_right:
                return None
            
            curr_val = preorder.pop(0)
            curr_node = TreeNode(curr_val)
            ind = indexer[curr_val]

            curr_node.left = helper(preorder, inorder_left, ind - 1)
            curr_node.right = helper(preorder, ind + 1, inorder_right)

            return curr_node
        
        return helper(preorder, 0, len(inorder) - 1)

Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
